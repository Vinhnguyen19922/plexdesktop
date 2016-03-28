# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browser.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Browser(object):
    def setupUi(self, Browser):
        Browser.setObjectName("Browser")
        Browser.resize(433, 550)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Browser)
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_back = QtWidgets.QPushButton(Browser)
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
        self.btn_reload = QtWidgets.QPushButton(Browser)
        self.btn_reload.setMaximumSize(QtCore.QSize(30, 16777215))
        self.btn_reload.setObjectName("btn_reload")
        self.horizontalLayout.addWidget(self.btn_reload)
        self.btn_home = QtWidgets.QPushButton(Browser)
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
        self.btn_on_deck = QtWidgets.QPushButton(Browser)
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
        self.btn_recently_added = QtWidgets.QPushButton(Browser)
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
        self.btn_channels = QtWidgets.QPushButton(Browser)
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
        self.btn_test = QtWidgets.QPushButton(Browser)
        self.btn_test.setObjectName("btn_test")
        self.horizontalLayout.addWidget(self.btn_test)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.sort = QtWidgets.QComboBox(Browser)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.sort.setFont(font)
        self.sort.setObjectName("sort")
        self.horizontalLayout.addWidget(self.sort)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_path = QtWidgets.QLabel(Browser)
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
        self.indicator = QtWidgets.QProgressBar(Browser)
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
        self.shortcuts = QtWidgets.QComboBox(Browser)
        self.shortcuts.setMinimumSize(QtCore.QSize(100, 0))
        self.shortcuts.setObjectName("shortcuts")
        self.horizontalLayout_2.addWidget(self.shortcuts)
        self.btn_add_shortcut = QtWidgets.QPushButton(Browser)
        self.btn_add_shortcut.setMaximumSize(QtCore.QSize(75, 16777215))
        self.btn_add_shortcut.setObjectName("btn_add_shortcut")
        self.horizontalLayout_2.addWidget(self.btn_add_shortcut)
        self.btn_view_mode = QtWidgets.QPushButton(Browser)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_view_mode.sizePolicy().hasHeightForWidth())
        self.btn_view_mode.setSizePolicy(sizePolicy)
        self.btn_view_mode.setMaximumSize(QtCore.QSize(20, 16777215))
        self.btn_view_mode.setObjectName("btn_view_mode")
        self.horizontalLayout_2.addWidget(self.btn_view_mode)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.list = ListView(Browser)
        self.list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.list.setObjectName("list")
        self.verticalLayout_2.addWidget(self.list)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.servers = QtWidgets.QComboBox(Browser)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.servers.setFont(font)
        self.servers.setObjectName("servers")
        self.horizontalLayout_4.addWidget(self.servers)
        self.users = QtWidgets.QComboBox(Browser)
        self.users.setObjectName("users")
        self.horizontalLayout_4.addWidget(self.users)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.btn_metadata = QtWidgets.QPushButton(Browser)
        self.btn_metadata.setObjectName("btn_metadata")
        self.horizontalLayout_4.addWidget(self.btn_metadata)
        self.zoom = QtWidgets.QSlider(Browser)
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
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.metadata_panel = QtWidgets.QWidget(Browser)
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
        self.verticalLayout_2.addWidget(self.metadata_panel)

        self.retranslateUi(Browser)
        QtCore.QMetaObject.connectSlotsByName(Browser)

    def retranslateUi(self, Browser):
        _translate = QtCore.QCoreApplication.translate
        Browser.setWindowTitle(_translate("Browser", "Browser"))
        self.btn_back.setText(_translate("Browser", "<"))
        self.btn_reload.setText(_translate("Browser", "R"))
        self.btn_home.setText(_translate("Browser", "home"))
        self.btn_on_deck.setText(_translate("Browser", "on deck"))
        self.btn_recently_added.setText(_translate("Browser", "recently added"))
        self.btn_channels.setText(_translate("Browser", "channels"))
        self.btn_test.setText(_translate("Browser", "-"))
        self.btn_add_shortcut.setText(_translate("Browser", "+ shortcut"))
        self.btn_view_mode.setText(_translate("Browser", "::"))
        self.btn_metadata.setText(_translate("Browser", "v"))

from browserlist import ListView
