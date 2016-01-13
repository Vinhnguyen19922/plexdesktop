import hashlib
from PyQt5.QtWidgets import QListWidget, QListWidgetItem
from PyQt5.QtGui import QPixmap, QIcon, QBrush, QPixmapCache, QColor
from PyQt5.QtCore import pyqtSignal, QObject, QSize, Qt, QObject, QThread, QSettings
from sqlcache import SqlCache
import plexdevices

class BrowserList(QListWidget):
    resize_signal = pyqtSignal()
    iconSizeChanged = pyqtSignal(QSize) # object has no attribute 'iconSizeChanged' on linux ?

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setIconSize(QSize(32, 32))
        self.current_container = None
        self.server = None

        self._thumb_thread = QThread()
        self._cache = SqlCache('thumb', access=False)
        self._cache.moveToThread(self._thumb_thread)
        self._thumb_thread.started.connect(self._cache.open)
        self._thumb_thread.finished.connect(self._cache.save)

    def icon_size(self, x):
        self.setIconSize(QSize(x, x))

    def setIconSize(self, size):
        # reimplemented because linux was being weird
        super(BrowserList, self).setIconSize(size)
        self.iconSizeChanged.emit(size)

    def closeEvent(self, event):
        self.reset()

    def reset(self):
        self._thumb_thread.quit()
        self._thumb_thread.wait()

    def resizeEvent(self, event):
        self.resize_signal.emit()

    def mousePressEvent(self, event):
        if event.buttons() & Qt.BackButton:
            event.ignore()
        else:
            super().mousePressEvent(event)

    def add_container(self, container):
        self.current_container = container
        self.server = container.server
        for media_object in container.children:
            self.addItem(BrowserListItem(media_object, thread=self._thumb_thread, cache=self._cache, parent=self))


class BrowserListItem(QListWidgetItem):

    def __init__(self, media_object, thread=None, cache=None, parent=None):
        super().__init__(parent=parent)
        self.media = media_object

        self.thumb = None
        self.parent = parent
 
        parent.iconSizeChanged.connect(self.resize)
        parent.resize_signal.connect(self.update_bg)

        if self.media.get('thumb', False):
            self.controller = Controller(thumb=True, thread=thread, cache=cache)
            self.controller.new_item.connect(self.update_img)
            self.controller.operate.emit(media_object)

        item_type = self.media.get('type', None)
        view_group = self.media.parent.get('viewGroup', None)
        mixed_parents = bool(int(self.media.parent.get('mixedParents', '0')))
        filters = bool(int(self.media.get('filters', '0')))
        is_library = self.media.parent.get('identifier', None) == 'com.plexapp.plugins.library'
        if filters or not is_library:
                t = self.media['title']
        else:
            if view_group == 'episode':
                t = ('{} - s{:02d}e{:02d} - {}'.format(self.media['grandparentTitle'],
                                                       int(self.media['parentIndex']),
                                                       int(self.media['index']),
                                                       self.media['title'])
                     if mixed_parents else
                     's{:02d}e{:02d} - {}'.format(int(self.media.parent['parentIndex']),
                                                      int(self.media['index']),
                                                      self.media['title']))
            elif view_group == 'season':
                t = ('{} - {}'.format(self.media.parent['parentTitle'], self.media['title'])
                     if mixed_parents else
                     self.media['title'])
            elif view_group == 'secondary':
                t = self.media['title']
            elif view_group == 'movie':
                t = '{} ({})'.format(self.media['title'], self.media['year'])
            elif view_group == 'album':
                t = '{} - {}'.format(self.media['parentTitle'], self.media['title'])
            elif view_group == 'track':
                t = '{} - {}'.format(self.media['index'], self.media['title'])
            else:
                if item_type == 'episode':
                    t = '{} - s{:02d}e{:02d} - {}'.format(self.media['grandparentTitle'],
                                                          int(self.media['parentIndex']),
                                                          int(self.media['index']),
                                                          self.media['title'])
                elif item_type == 'season':
                    t = '{} - {}'.format(self.media['parentTitle'], self.media['title'])
                elif item_type == 'movie':
                    t = '{} ({})'.format(self.media['title'], self.media['year'])
                else:
                    t = self.media['title']
        self.setText(t)
        self.update_bg()

    def update_bg(self, offset=None):
        if (('viewOffset' not in self.media) or
                ('duration' not in self.media) or
                (self.media['viewOffset'] == 0)):
            return
        try:
            vo = int(self.media['viewOffset']) if offset is None else offset
            x = int(vo / int(self.media['duration']) * 100)
            xpm = ["100 1 2 1",   # 100x1 image
                   "a c #EEEEEE", # dark color
                   "b c #FFFFFF", # light color
                   "a"*x + "b"*(100-x)
                  ]
            self.setBackground(QBrush(QPixmap(xpm).scaled(self.parent.width(), 1)))
        except Exception as e:
            print(str(e))

    def update_offset(self, offset):
        self.media['viewOffset'] = offset
        self.update_bg(offset)

    def clear_bg(self):
        self.setBackground(QBrush(QColor(255, 255, 255)))

    def update_img(self, pixmap):
        self.controller = None
        if not pixmap.isNull():
            self.thumb = pixmap
            self.resize(self.parent.iconSize())

    def resize(self, size):
        if self.thumb is not None:
            self.setIcon(QIcon(self.thumb.scaled(size, Qt.KeepAspectRatio)))


class Controller(QObject):
    operate = pyqtSignal(plexdevices.MediaObject)
    new_item = pyqtSignal(QPixmap)   

    def __init__(self, thumb=False, thread=None, cache=None, parent=None):
        super().__init__(parent=parent)
        self.worker_thread = thread
        self.worker = ImgWorker(thumb, cache)
        self.worker.moveToThread(self.worker_thread)
        self.operate.connect(self.worker.do_work)
        self.worker.result_ready.connect(self.handle_results)
        self.worker_thread.start()

    def handle_results(self, item):
        self.new_item.emit(item)
        self.worker = None


class ImgWorker(QObject):
    result_ready = pyqtSignal(QPixmap)

    def __init__(self, thumb=False, cache=None, parent=None):
        super().__init__()
        self.thumb = thumb
        self.cache = cache

    def do_work(self, media_object):
        url = media_object['thumb'] if self.thumb else media_object.resolve_url()
        key = media_object.parent.server.client_identifier + url
        key_hash = hashlib.md5(key.encode('utf-8')).hexdigest()
        img = QPixmapCache.find(key_hash)
        if img is None:
            img_data = self.cache[url]
            if img_data is None:
                img_data = media_object.parent.server.image(url, w=300, h=300)
                self.cache[url] = img_data
            img = QPixmap()
            img.loadFromData(img_data)
            QPixmapCache.insert(key_hash, img)
        self.result_ready.emit(img)
        return
