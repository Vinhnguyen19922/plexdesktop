# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plexdesktop\ui\remote.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Remote(object):
    def setupUi(self, Remote):
        Remote.setObjectName("Remote")
        Remote.resize(533, 253)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Remote)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalWidget_2 = QtWidgets.QWidget(Remote)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget_2.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_2.setSizePolicy(sizePolicy)
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.horizontalWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_back = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.btn_back.setObjectName("btn_back")
        self.gridLayout_2.addWidget(self.btn_back, 2, 0, 1, 1)
        self.btn_down = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.btn_down.setObjectName("btn_down")
        self.gridLayout_2.addWidget(self.btn_down, 2, 1, 1, 1)
        self.btn_left = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.btn_left.setObjectName("btn_left")
        self.gridLayout_2.addWidget(self.btn_left, 1, 0, 1, 1)
        self.btn_select = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.btn_select.setObjectName("btn_select")
        self.gridLayout_2.addWidget(self.btn_select, 1, 1, 1, 1)
        self.btn_right = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.btn_right.setObjectName("btn_right")
        self.gridLayout_2.addWidget(self.btn_right, 1, 2, 1, 1)
        self.btn_up = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.btn_up.setObjectName("btn_up")
        self.gridLayout_2.addWidget(self.btn_up, 0, 1, 1, 1)
        self.btn_home = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.btn_home.setObjectName("btn_home")
        self.gridLayout_2.addWidget(self.btn_home, 0, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.progress = QtWidgets.QSlider(self.horizontalWidget_2)
        self.progress.setOrientation(QtCore.Qt.Horizontal)
        self.progress.setObjectName("progress")
        self.verticalLayout_3.addWidget(self.progress)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_skip_prev = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.btn_skip_prev.setObjectName("btn_skip_prev")
        self.horizontalLayout.addWidget(self.btn_skip_prev)
        self.btn_play = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.btn_play.setObjectName("btn_play")
        self.horizontalLayout.addWidget(self.btn_play)
        self.btn_pause = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.btn_pause.setObjectName("btn_pause")
        self.horizontalLayout.addWidget(self.btn_pause)
        self.btn_stop = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.btn_stop.setObjectName("btn_stop")
        self.horizontalLayout.addWidget(self.btn_stop)
        self.btn_skip_next = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.btn_skip_next.setObjectName("btn_skip_next")
        self.horizontalLayout.addWidget(self.btn_skip_next)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.lbl_timeline = QtWidgets.QLabel(self.horizontalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_timeline.sizePolicy().hasHeightForWidth())
        self.lbl_timeline.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(5)
        self.lbl_timeline.setFont(font)
        self.lbl_timeline.setText("")
        self.lbl_timeline.setWordWrap(True)
        self.lbl_timeline.setObjectName("lbl_timeline")
        self.verticalLayout_3.addWidget(self.lbl_timeline)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_3.addWidget(self.horizontalWidget_2)
        self.verticalWidget = QtWidgets.QWidget(Remote)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lbl_title = QtWidgets.QLabel(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_title.sizePolicy().hasHeightForWidth())
        self.lbl_title.setSizePolicy(sizePolicy)
        self.lbl_title.setText("")
        self.lbl_title.setWordWrap(True)
        self.lbl_title.setObjectName("lbl_title")
        self.verticalLayout_4.addWidget(self.lbl_title)
        self.lbl_summary = QtWidgets.QLabel(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_summary.sizePolicy().hasHeightForWidth())
        self.lbl_summary.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.lbl_summary.setFont(font)
        self.lbl_summary.setText("")
        self.lbl_summary.setWordWrap(True)
        self.lbl_summary.setObjectName("lbl_summary")
        self.verticalLayout_4.addWidget(self.lbl_summary)
        self.lbl_image = QtWidgets.QLabel(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_image.sizePolicy().hasHeightForWidth())
        self.lbl_image.setSizePolicy(sizePolicy)
        self.lbl_image.setText("")
        self.lbl_image.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_image.setScaledContents(True)
        self.lbl_image.setWordWrap(True)
        self.lbl_image.setObjectName("lbl_image")
        self.verticalLayout_4.addWidget(self.lbl_image)
        self.horizontalLayout_3.addWidget(self.verticalWidget)

        self.retranslateUi(Remote)
        QtCore.QMetaObject.connectSlotsByName(Remote)

    def retranslateUi(self, Remote):
        _translate = QtCore.QCoreApplication.translate
        Remote.setWindowTitle(_translate("Remote", "Remote"))
        self.btn_back.setText(_translate("Remote", "< Back"))
        self.btn_down.setText(_translate("Remote", "v"))
        self.btn_left.setText(_translate("Remote", "<"))
        self.btn_select.setText(_translate("Remote", "O"))
        self.btn_right.setText(_translate("Remote", ">"))
        self.btn_up.setText(_translate("Remote", "^"))
        self.btn_home.setText(_translate("Remote", "Home"))
        self.btn_skip_prev.setText(_translate("Remote", "< skip"))
        self.btn_play.setText(_translate("Remote", "play"))
        self.btn_pause.setText(_translate("Remote", "pause"))
        self.btn_stop.setText(_translate("Remote", "stop"))
        self.btn_skip_next.setText(_translate("Remote", "skip >"))

