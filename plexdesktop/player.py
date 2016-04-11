import logging
from PyQt5.QtWidgets import QWidget, QInputDialog, QMainWindow, QAction, QMenu
from PyQt5.QtCore import (pyqtSignal, pyqtSlot, Qt, QThread, QPoint, QSize,
                          QObject, QTimer, QElapsedTimer)
from PyQt5.QtGui import QCursor
from plexdesktop.ui.player_ui import Ui_Player
from plexdesktop.settings import Settings
from plexdesktop.browserlist import ListView
import plexdesktop.utils as utils
import mpv
import plexdevices
mpv.load_library()
logger = logging.getLogger('plexdesktop')
mpv_logger = logging.getLogger('plexdesktop.mpv')

MPV_TO_LOGGING = {
    'fatal': logging.CRITICAL,
    'error': logging.ERROR,
    'warn': logging.WARNING,
    'info': logging.INFO,
    'v': 15,
    'debug': logging.DEBUG,
    'trace': 5
}


class PlexMpv(mpv.MpvTemplatePyQt):
    prop_duration = pyqtSignal(float)
    prop_volume = pyqtSignal(float)
    prop_playback_time = pyqtSignal(float)
    prop_track_list = pyqtSignal(list)
    prop_video_params = pyqtSignal(dict)
    next_item = pyqtSignal(plexdevices.MediaItem)
    update_timeline = pyqtSignal(plexdevices.PlayQueue, plexdevices.MediaItem,
                                 float, dict, str)
    shutdown = pyqtSignal()
    play_queue_updated = pyqtSignal(plexdevices.PlayQueue)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._timeline_thread = QThread(self)
        self._timeline_updater = TimelineUpdater()
        self._timeline_updater.moveToThread(self._timeline_thread)
        self.update_timeline.connect(self._timeline_updater.update)
        self._timeline_thread.finished.connect(self._timeline_thread.deleteLater)
        self._timeline_thread.start()

        self.plex_play_queue = None
        self.plex_current_item = None
        self.plex_next_item = None

        self.timeline_timer = QElapsedTimer()

    @property
    def headers(self):
        return {'X-Plex-Client-Identifier': 'test1',
                'X-Plex-Device-Name': 'plexdesktop player'}

    def create_play_queue(self, media_object):
        self.plex_play_queue = plexdevices.PlayQueue.create(media_object, self.headers)
        self.plex_current_item = (self.plex_play_queue.selected_item
                                  if self.plex_play_queue.selected_item is not None
                                  else media_object)
        self.play_queue_updated.emit(self.plex_play_queue)

    def on_shutdown(self, event):
        super().on_shutdown(event)
        self._timeline_thread.quit()
        self._timeline_thread.wait()
        self.shutdown.emit()

    def on_log_message(self, event):
        msg = '{e[prefix]}: {e[text]}'.format(e=event)
        self.log_handler.log(MPV_TO_LOGGING[event['level']], msg)

    def on_start_file(self, event):
        self.timeline_timer.restart()

    def on_end_file(self, event):
        self.log_handler.debug('Player: do_end_file')
        item = (self.plex_play_queue.get_next() if self.plex_next_item is None else
                self.plex_play_queue.select(self.plex_next_item))
        if item is not None:
            self.plex_current_item = item
            self.plex_next_item = None
            self.next_item.emit(item)

    def on_property_change(self, event):
        if event['data'] is None:
            self.log_handler.debug('property change with no data: event={}'.format(event))
            return
        if event['name'] == 'pause':
            try:
                cur_time = self.mpv.playback_time
            except mpv.MpvError:
                return
            state = 'paused' if event['data'] else 'playing'
            self.update_timeline.emit(self.plex_play_queue, self.plex_current_item,
                                      cur_time, self.headers, state)
        elif event['name'] == 'duration':
            self.prop_duration.emit(event['data'])
        elif event['name'] == 'volume':
            self.prop_volume.emit(event['data'])
        elif event['name'] == 'playback-time':
            self.prop_playback_time.emit(event['data'])
            if self.timeline_timer.elapsed() > 15000:
                self.update_timeline.emit(self.plex_play_queue, self.plex_current_item,
                                          event['data'], self.headers, 'playing')
                self.timeline_timer.restart()
        elif event['name'] == 'track-list':
            self.prop_track_list.emit(event['data'])
        elif event['name'] == 'video-params':
            self.prop_video_params.emit(event['data'])
        elif event['name'] == 'video-out-params':
            self.log_handler.debug('video-out-params: {}'.format(event['data']))
        elif event['name'] == 'metadata':
            self.log_handler.debug('metadata: {}'.format(event['data']))
        elif event['name'] == 'chapter-metadata':
            self.log_handler.debug('chapter-metadata: {}'.format(event['data']))

    def play(self, url, args):
        self.mpv.command_node('loadfile', url, 'replace', args)

    @pyqtSlot()
    def pause(self):
        self.mpv.pause = not self.mpv.pause

    @pyqtSlot(str)
    def change_audio_track(self, tid):
        logger.debug('changing audio track: {}'.format(tid))
        self.mpv.aid = tid

    @pyqtSlot(str)
    def change_video_track(self, tid):
        logger.debug('changing video track: {}'.format(tid))
        self.mpv.vid = tid

    @pyqtSlot(str)
    def change_sub_track(self, tid):
        logger.debug('changing sub tid: {}'.format(tid))
        if tid == '-1':
            self.mpv.sub_visibility = False
        else:
            self.mpv.sid = tid
            self.mpv.sub_visibility = True

    @pyqtSlot()
    def playlist_prev(self):
        self.playlist_play_item(self.plex_play_queue.get_prev())

    @pyqtSlot()
    def playlist_next(self):
        self.playlist_play_item(self.plex_play_queue.get_next())

    @pyqtSlot(plexdevices.MediaItem)
    def playlist_play_item(self, item):
        self.plex_next_item = item
        self.mpv.stop()  # trigger an end_file

    @pyqtSlot(plexdevices.MediaItem)
    def playlist_skip_to(self, item):
        self.playlist_play_item(self.plex_play_queue.select(item))

    def playlist_queue_item(self, item):
        if self.plex_play_queue is not None:
            self.plex_play_queue.add_item(item, self.headers)
            self.play_queue_updated.emit(self.plex_play_queue)

    def playlist_remove_item(self, checked=False, item=None):
        if self.plex_play_queue is not None:
            if item is None:
                item = self.sender().data()
            self.plex_play_queue.remove_item(item)
            self.play_queue_updated.emit(self.plex_play_queue)


class TimelineUpdater(QObject):
    finished = pyqtSignal()

    def update(self, play_queue, item, time, headers, state='playing'):
        play_queue.timeline_update(item, int(time * 1000), headers, state)
        self.finished.emit()


class PlayerUI(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Player()
        self.ui.setupUi(self)
        self.ui.player_widget.setAttribute(Qt.WA_DontCreateNativeAncestors)
        self.ui.player_widget.setAttribute(Qt.WA_NativeWindow)
        self.ui.player_widget.setMouseTracking(True)
        self.ui.slider_volume.setMaximum(100)
        self.ui.audio_tracks.set_type('audio')
        self.ui.sub_tracks.set_type('sub')
        self.ui.video_tracks.set_type('video')
        # for convenience
        self.controls = self.ui
        self.player = self.ui.player_widget
        self.control_bar = self.ui.control_bar

    @pyqtSlot(float)
    def update_seek_slider_position(self, val):
        if not self.ui.slider_progress.isSliderDown():
            self.ui.slider_progress.setSliderPosition(val * 1000)

    @pyqtSlot(float)
    def update_seek_slider_maximum(self, val):
        self.ui.slider_progress.setMaximum(val * 1000)

    @pyqtSlot(float)
    def update_lbl_total_time(self, val):
        self.ui.lbl_total_time.setText(utils.timestamp_from_ms(milliseconds=val * 1000.0))

    @pyqtSlot(float)
    def update_lbl_current_time(self, val):
        self.ui.lbl_current_time.setText(utils.timestamp_from_ms(milliseconds=val * 1000.0))


class MPVPlayer(QMainWindow):
    player_stopped = pyqtSignal()
    mouse_moved = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = PlayerUI(self)
        self.setCentralWidget(self.ui)

        self.playlist = ListView()
        self.playlist.setWindowTitle('Playlist')
        self.playlist.setContextMenuPolicy(Qt.CustomContextMenu)

        menu = self.menuBar().addMenu('&File')
        on_quit = QAction('&Quit', self)
        on_quit.triggered.connect(self.on_quit)
        menu.addAction(on_quit)

        menu_view = self.menuBar().addMenu('&View')
        on_playlist = QAction('&Playlist', self)
        on_playlist.triggered.connect(self.on_playlist)
        menu_view.addAction(on_playlist)

        # MPV setup
        wid = int(self.ui.player.winId())
        self.mpv = PlexMpv(self)
        self.mpv.initialize(wid=wid,
                            log_handler=mpv_logger,
                            log_level=mpv.MpvLogLevel.INFO,
                            input_cursor='no',
                            cache_backbuffer=10 * 1024,
                            cache_default=25 * 1024,
                            demuxer_max_bytes=50 * 1024 * 1024,
                            hwdec='auto',
                            observe=['pause', 'playback-time', 'duration',
                                     'track-list', 'video-params',
                                     'video-out-params', 'metadata',
                                     'chapter-metadata'])

        # cursor hiding
        self.setMouseTracking(True)
        self.cursor_timer = QTimer()
        self.cursor_timer.setSingleShot(True)
        self.cursor_timer.setInterval(1000)
        self.cursor_timer.timeout.connect(self.hide_cursor)
        self.mouse_moved.connect(self.cursor_timer.start)

        self.settings = Settings()
        self.drag_position = None
        self.resized = False

        # Restore saved volume
        try:
            last_vol = self.settings.value('last_volume', 0.0)
            self.mpv.volume = last_vol
            self.ui.controls.slider_volume.setValue(last_vol * 10)
        except Exception:
            pass

        self.mpv.next_item.connect(self.play)

        self.mpv.play_queue_updated.connect(self.playlist.add_container2)
        # observed properties
        self.mpv.prop_video_params.connect(self.resize_to_vid)
        self.mpv.prop_duration.connect(self.ui.update_seek_slider_maximum)
        self.mpv.prop_duration.connect(self.ui.update_lbl_total_time)
        self.mpv.prop_playback_time.connect(self.ui.update_seek_slider_position)
        self.mpv.prop_playback_time.connect(self.ui.update_lbl_current_time)
        self.mpv.prop_track_list.connect(self.ui.controls.audio_tracks.update_tracks)
        self.mpv.prop_track_list.connect(self.ui.controls.video_tracks.update_tracks)
        self.mpv.prop_track_list.connect(self.ui.controls.sub_tracks.update_tracks)
        # buttons
        self.ui.controls.btn_prev.pressed.connect(self.mpv.playlist_prev)
        self.ui.controls.btn_next.pressed.connect(self.mpv.playlist_next)
        self.ui.controls.btn_play.clicked.connect(self.mpv.pause)
        # track selector combo boxes
        self.ui.controls.audio_tracks.trackChanged.connect(self.mpv.change_audio_track)
        self.ui.controls.sub_tracks.trackChanged.connect(self.mpv.change_sub_track)
        self.ui.controls.video_tracks.trackChanged.connect(self.mpv.change_video_track)
        # sliders
        self.ui.controls.slider_volume.valueChanged.connect(self.slider_volume)
        self.ui.controls.slider_progress.sliderReleased.connect(self.slider_seek)

        self.mpv.shutdown.connect(self.player_stopped.emit)

        self.playlist.customContextMenuRequested.connect(self.playlist_context_menu)
        self.playlist.itemDoubleClicked.connect(self.playlist_item_double_clicked)

    @pyqtSlot()
    def on_quit(self):
        self.close()

    @pyqtSlot()
    def on_playlist(self):
        self.playlist.setVisible(not self.playlist.isVisible())

    @pyqtSlot(int)
    def slider_volume(self, val, f=10):
        slider_max = self.ui.controls.slider_volume.maximum()
        self.mpv.set_volume(100.0 * (f**(val / slider_max) - 1) / (f - 1))

    @pyqtSlot()
    def slider_seek(self):
        self.mpv.seek_absolute(self.ui.controls.slider_progress.value())

    @pyqtSlot(dict)
    def resize_to_vid(self, video_params):
        if not self.resized:
            if 'w' not in video_params and 'h' not in video_params:
                return
            self.resized = True
            self.resize(QSize(video_params['w'],
                              video_params['h'] + self.ui.control_bar.height() +
                              self.menuBar().height()))

    @pyqtSlot('QPoint')
    def playlist_context_menu(self, pos):
        item = self.playlist.currentItem()
        menu = QMenu(self)
        remove = QAction('Remove', menu)
        remove.triggered.connect(self.mpv.playlist_remove_item)
        remove.setData(item)
        menu.addAction(remove)
        if not menu.isEmpty():
            menu.exec_(QCursor.pos())

    @pyqtSlot(plexdevices.MediaItem)
    def playlist_item_double_clicked(self, item):
        self.mpv.playlist_skip_to(item)

    @pyqtSlot()
    def hide_cursor(self):
        if self.isFullScreen():
            self.setCursor(Qt.BlankCursor)

    @pyqtSlot(plexdevices.MediaItem)
    def queue(self, media_object):
        self.mpv.playlist_queue_item(media_object)

    @pyqtSlot(plexdevices.MediaItem)
    def play(self, media_object):
        if self.mpv.plex_play_queue is None:
            self.mpv.create_play_queue(media_object)
        logger.info('Player: playQueueID={}'.format(self.mpv.plex_play_queue.id))

        self.setWindowTitle(utils.title(self.mpv.plex_current_item))

        if len(self.mpv.plex_current_item.media) == 1:
            url = self.mpv.plex_current_item.media[0].parts[0].resolve_key()
        else:
            options = [str(x.height) for x in self.mpv.plex_current_item.media]
            choice, ok = QInputDialog.getItem(self, 'QInputDialog.getItem()',
                                              'Stream:', options, 0, False)
            if ok:
                index = options.index(choice)
                url = self.mpv.plex_current_item.media[index].parts[0].resolve_key()
            else:
                self.close()
                return

        logger.info('Player: playing url: ' + url)

        args = {}
        if self.mpv.plex_current_item.view_offset:
            args['start'] = '+{}'.format(self.mpv.plex_current_item.view_offset / 1000.0)
        if isinstance(self.mpv.plex_current_item, plexdevices.Track):
            args['vid'] = 'no'

        self.mpv.play(url, args)

    def toggle_control_bar(self):
        self.ui.control_bar.setVisible(not self.ui.control_bar.isVisible())
        self.menuBar().setVisible(not self.menuBar().isVisible())

    # QT EVENTS ################################################################
    def closeEvent(self, event):
        self.playlist.close()
        self.settings.setValue('last_volume', self.ui.controls.slider_volume.value() / 10.0)
        self.mpv.quit()

    def wheelEvent(self, event):
        degrees = event.angleDelta().y() / 8
        steps = int(degrees / 15)
        self.ui.controls.slider_volume.setSliderPosition(self.ui.controls.slider_volume.value() + steps)
        event.accept()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:  # window dragging
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        self.unsetCursor()
        if self.isFullScreen():
            self.mouse_moved.emit()
        if event.buttons() & Qt.LeftButton:
            if not self.isFullScreen() and self.drag_position is not None:  # window dragging
                self.move(event.globalPos() - self.drag_position)
                event.accept()

    def mouseDoubleClickEvent(self, event):
        if not self.isFullScreen():
            self.showFullScreen()
            self.ui.control_bar.hide()
            self.menuBar().hide()
        else:
            self.showNormal()
            self.ui.control_bar.show()
            self.menuBar().show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.mpv.pause()
        elif event.key() == Qt.Key_QuoteLeft:
            self.toggle_control_bar()
