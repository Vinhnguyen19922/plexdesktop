# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plexdesktop\ui\browser.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Browser(object):
    def setupUi(self, Browser):
        Browser.setObjectName("Browser")
        Browser.resize(425, 289)
        self.centralwidget = QtWidgets.QWidget(Browser)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_back.sizePolicy().hasHeightForWidth())
        self.btn_back.setSizePolicy(sizePolicy)
        self.btn_back.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout.addWidget(self.btn_back)
        self.btn_reload = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reload.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.btn_reload.setFont(font)
        self.btn_reload.setObjectName("btn_reload")
        self.horizontalLayout.addWidget(self.btn_reload)
        self.btn_home = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.btn_home.setFont(font)
        self.btn_home.setObjectName("btn_home")
        self.horizontalLayout.addWidget(self.btn_home)
        self.btn_on_deck = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_on_deck.sizePolicy().hasHeightForWidth())
        self.btn_on_deck.setSizePolicy(sizePolicy)
        self.btn_on_deck.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.btn_on_deck.setFont(font)
        self.btn_on_deck.setObjectName("btn_on_deck")
        self.horizontalLayout.addWidget(self.btn_on_deck)
        self.btn_recently_added = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_recently_added.sizePolicy().hasHeightForWidth())
        self.btn_recently_added.setSizePolicy(sizePolicy)
        self.btn_recently_added.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.btn_recently_added.setFont(font)
        self.btn_recently_added.setObjectName("btn_recently_added")
        self.horizontalLayout.addWidget(self.btn_recently_added)
        self.btn_channels = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_channels.sizePolicy().hasHeightForWidth())
        self.btn_channels.setSizePolicy(sizePolicy)
        self.btn_channels.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.btn_channels.setFont(font)
        self.btn_channels.setObjectName("btn_channels")
        self.horizontalLayout.addWidget(self.btn_channels)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.sort = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.sort.setFont(font)
        self.sort.setObjectName("sort")
        self.horizontalLayout.addWidget(self.sort)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_path = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_path.sizePolicy().hasHeightForWidth())
        self.lbl_path.setSizePolicy(sizePolicy)
        self.lbl_path.setText("")
        self.lbl_path.setObjectName("lbl_path")
        self.horizontalLayout_2.addWidget(self.lbl_path)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.indicator = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.indicator.sizePolicy().hasHeightForWidth())
        self.indicator.setSizePolicy(sizePolicy)
        self.indicator.setMaximumSize(QtCore.QSize(30, 16777215))
        self.indicator.setMaximum(0)
        self.indicator.setProperty("value", -1)
        self.indicator.setTextVisible(False)
        self.indicator.setInvertedAppearance(False)
        self.indicator.setObjectName("indicator")
        self.horizontalLayout_2.addWidget(self.indicator)
        self.shortcuts = QtWidgets.QComboBox(self.centralwidget)
        self.shortcuts.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.shortcuts.setFont(font)
        self.shortcuts.setObjectName("shortcuts")
        self.horizontalLayout_2.addWidget(self.shortcuts)
        self.btn_add_shortcut = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add_shortcut.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.btn_add_shortcut.setFont(font)
        self.btn_add_shortcut.setObjectName("btn_add_shortcut")
        self.horizontalLayout_2.addWidget(self.btn_add_shortcut)
        self.btn_view_mode = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_view_mode.sizePolicy().hasHeightForWidth())
        self.btn_view_mode.setSizePolicy(sizePolicy)
        self.btn_view_mode.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.btn_view_mode.setFont(font)
        self.btn_view_mode.setObjectName("btn_view_mode")
        self.horizontalLayout_2.addWidget(self.btn_view_mode)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.list = ListView(self.centralwidget)
        self.list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.list.setObjectName("list")
        self.verticalLayout.addWidget(self.list)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.servers = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.servers.setFont(font)
        self.servers.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.servers.setObjectName("servers")
        self.horizontalLayout_4.addWidget(self.servers)
        self.users = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.users.setFont(font)
        self.users.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.users.setObjectName("users")
        self.horizontalLayout_4.addWidget(self.users)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.btn_metadata = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.btn_metadata.setFont(font)
        self.btn_metadata.setObjectName("btn_metadata")
        self.horizontalLayout_4.addWidget(self.btn_metadata)
        self.zoom = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoom.sizePolicy().hasHeightForWidth())
        self.zoom.setSizePolicy(sizePolicy)
        self.zoom.setMinimumSize(QtCore.QSize(125, 0))
        self.zoom.setMinimum(24)
        self.zoom.setMaximum(300)
        self.zoom.setProperty("value", 32)
        self.zoom.setSliderPosition(32)
        self.zoom.setOrientation(QtCore.Qt.Horizontal)
        self.zoom.setObjectName("zoom")
        self.horizontalLayout_4.addWidget(self.zoom)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.metadata_panel = QtWidgets.QWidget(self.centralwidget)
        self.metadata_panel.setEnabled(True)
        self.metadata_panel.setObjectName("metadata_panel")
        self.grid_layout_2 = QtWidgets.QGridLayout(self.metadata_panel)
        self.grid_layout_2.setContentsMargins(0, 0, 0, 0)
        self.grid_layout_2.setSpacing(0)
        self.grid_layout_2.setObjectName("grid_layout_2")
        self.lbl_metadata = QtWidgets.QLabel(self.metadata_panel)
        self.lbl_metadata.setText("")
        self.lbl_metadata.setWordWrap(True)
        self.lbl_metadata.setObjectName("lbl_metadata")
        self.grid_layout_2.addWidget(self.lbl_metadata, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.metadata_panel)
        Browser.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Browser)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 425, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSession = QtWidgets.QMenu(self.menubar)
        self.menuSession.setObjectName("menuSession")
        self.menuRemotes = QtWidgets.QMenu(self.menuSession)
        self.menuRemotes.setObjectName("menuRemotes")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        Browser.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Browser)
        self.statusbar.setObjectName("statusbar")
        Browser.setStatusBar(self.statusbar)
        self.actionPreferences = QtWidgets.QAction(Browser)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionLogin_Refresh = QtWidgets.QAction(Browser)
        self.actionLogin_Refresh.setEnabled(True)
        self.actionLogin_Refresh.setObjectName("actionLogin_Refresh")
        self.actionQuit = QtWidgets.QAction(Browser)
        self.actionQuit.setObjectName("actionQuit")
        self.actionInfo = QtWidgets.QAction(Browser)
        self.actionInfo.setEnabled(True)
        self.actionInfo.setObjectName("actionInfo")
        self.actionLogout = QtWidgets.QAction(Browser)
        self.actionLogout.setObjectName("actionLogout")
        self.actionAbout = QtWidgets.QAction(Browser)
        self.actionAbout.setObjectName("actionAbout")
        self.actionReload_Stylesheet = QtWidgets.QAction(Browser)
        self.actionReload_Stylesheet.setObjectName("actionReload_Stylesheet")
        self.actionAdd_Server = QtWidgets.QAction(Browser)
        self.actionAdd_Server.setObjectName("actionAdd_Server")
        self.actionTrim_Image_Cache = QtWidgets.QAction(Browser)
        self.actionTrim_Image_Cache.setObjectName("actionTrim_Image_Cache")
        self.actionTrim_Thumb_Cache = QtWidgets.QAction(Browser)
        self.actionTrim_Thumb_Cache.setObjectName("actionTrim_Thumb_Cache")
        self.actionRefresh_Devices = QtWidgets.QAction(Browser)
        self.actionRefresh_Devices.setObjectName("actionRefresh_Devices")
        self.actionRefresh_Users = QtWidgets.QAction(Browser)
        self.actionRefresh_Users.setObjectName("actionRefresh_Users")
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionPreferences)
        self.menuEdit.addAction(self.actionReload_Stylesheet)
        self.menuEdit.addAction(self.actionTrim_Image_Cache)
        self.menuEdit.addAction(self.actionTrim_Thumb_Cache)
        self.menuRemotes.addSeparator()
        self.menuSession.addAction(self.actionLogin_Refresh)
        self.menuSession.addAction(self.actionInfo)
        self.menuSession.addAction(self.actionLogout)
        self.menuSession.addAction(self.menuRemotes.menuAction())
        self.menuSession.addAction(self.actionAdd_Server)
        self.menuSession.addAction(self.actionRefresh_Devices)
        self.menuSession.addAction(self.actionRefresh_Users)
        self.menu_Help.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSession.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(Browser)
        QtCore.QMetaObject.connectSlotsByName(Browser)

    def retranslateUi(self, Browser):
        _translate = QtCore.QCoreApplication.translate
        Browser.setWindowTitle(_translate("Browser", "plexdesktop"))
        self.btn_back.setText(_translate("Browser", "<"))
        self.btn_reload.setText(_translate("Browser", "R"))
        self.btn_home.setText(_translate("Browser", "home"))
        self.btn_on_deck.setText(_translate("Browser", "on deck"))
        self.btn_recently_added.setText(_translate("Browser", "recently added"))
        self.btn_channels.setText(_translate("Browser", "channels"))
        self.btn_add_shortcut.setText(_translate("Browser", "+ shortcut"))
        self.btn_view_mode.setText(_translate("Browser", "::"))
        self.btn_metadata.setText(_translate("Browser", "v"))
        self.menuFile.setTitle(_translate("Browser", "&File"))
        self.menuEdit.setTitle(_translate("Browser", "&Edit"))
        self.menuSession.setTitle(_translate("Browser", "&Session"))
        self.menuRemotes.setTitle(_translate("Browser", "Remotes"))
        self.menu_Help.setTitle(_translate("Browser", "&Help"))
        self.actionPreferences.setText(_translate("Browser", "&Preferences"))
        self.actionLogin_Refresh.setText(_translate("Browser", "&Login/Refresh..."))
        self.actionQuit.setText(_translate("Browser", "&Quit"))
        self.actionInfo.setText(_translate("Browser", "&Info"))
        self.actionLogout.setText(_translate("Browser", "Log&out"))
        self.actionAbout.setText(_translate("Browser", "&About"))
        self.actionReload_Stylesheet.setText(_translate("Browser", "&Reload Stylesheet"))
        self.actionAdd_Server.setText(_translate("Browser", "Add Server..."))
        self.actionTrim_Image_Cache.setText(_translate("Browser", "Trim Image Cache"))
        self.actionTrim_Thumb_Cache.setText(_translate("Browser", "Trim Thumb Cache"))
        self.actionRefresh_Devices.setText(_translate("Browser", "Refresh Devices..."))
        self.actionRefresh_Users.setText(_translate("Browser", "Refresh Users..."))

from plexdesktop.browserlist import ListView
