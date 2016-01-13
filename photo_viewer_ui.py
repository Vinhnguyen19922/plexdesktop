# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'photo_viewer.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PhotoViewer(object):
    def setupUi(self, PhotoViewer):
        PhotoViewer.setObjectName("PhotoViewer")
        PhotoViewer.resize(466, 404)
        PhotoViewer.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(PhotoViewer)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.control_bar = QtWidgets.QWidget(PhotoViewer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.control_bar.sizePolicy().hasHeightForWidth())
        self.control_bar.setSizePolicy(sizePolicy)
        self.control_bar.setStyleSheet("")
        self.control_bar.setObjectName("control_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.control_bar)
        self.horizontalLayout.setContentsMargins(-1, 0, 1, 0)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_prev = QtWidgets.QPushButton(self.control_bar)
        self.btn_prev.setObjectName("btn_prev")
        self.horizontalLayout.addWidget(self.btn_prev)
        self.btn_next = QtWidgets.QPushButton(self.control_bar)
        self.btn_next.setObjectName("btn_next")
        self.horizontalLayout.addWidget(self.btn_next)
        self.btn_refresh = QtWidgets.QPushButton(self.control_bar)
        self.btn_refresh.setObjectName("btn_refresh")
        self.horizontalLayout.addWidget(self.btn_refresh)
        self.indicator = QtWidgets.QProgressBar(self.control_bar)
        self.indicator.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.indicator.sizePolicy().hasHeightForWidth())
        self.indicator.setSizePolicy(sizePolicy)
        self.indicator.setMaximumSize(QtCore.QSize(30, 16777215))
        self.indicator.setMaximum(0)
        self.indicator.setProperty("value", -1)
        self.indicator.setTextVisible(False)
        self.indicator.setObjectName("indicator")
        self.horizontalLayout.addWidget(self.indicator)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.control_bar)
        self.horizontalWidget = QtWidgets.QWidget(PhotoViewer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalWidget.setStyleSheet("background-color:black;")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.viewer = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.viewer.setContentsMargins(0, 0, 0, 0)
        self.viewer.setSpacing(0)
        self.viewer.setObjectName("viewer")
        self.image_label = AspectRatioLabel(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setObjectName("image_label")
        self.viewer.addWidget(self.image_label)
        self.verticalLayout.addWidget(self.horizontalWidget)

        self.retranslateUi(PhotoViewer)
        QtCore.QMetaObject.connectSlotsByName(PhotoViewer)

    def retranslateUi(self, PhotoViewer):
        _translate = QtCore.QCoreApplication.translate
        PhotoViewer.setWindowTitle(_translate("PhotoViewer", "Form"))
        self.btn_prev.setText(_translate("PhotoViewer", "<"))
        self.btn_next.setText(_translate("PhotoViewer", ">"))
        self.btn_refresh.setText(_translate("PhotoViewer", "refresh"))
        self.image_label.setText(_translate("PhotoViewer", "TextLabel"))

from extra_widgets import AspectRatioLabel
