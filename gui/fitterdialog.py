# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/qt\fitterdialog.ui'
#
# Created: Sun Apr 24 21:40:25 2016
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fitterDialog(object):
    def setupUi(self, fitterDialog):
        fitterDialog.setObjectName("fitterDialog")
        fitterDialog.resize(800, 640)
        self.verticalLayout = QtWidgets.QVBoxLayout(fitterDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.openButton = QtWidgets.QPushButton(fitterDialog)
        self.openButton.setObjectName("openButton")
        self.horizontalLayout_2.addWidget(self.openButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(fitterDialog)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(fitterDialog)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.zoomSlider = QtWidgets.QSlider(fitterDialog)
        self.zoomSlider.setOrientation(QtCore.Qt.Horizontal)
        self.zoomSlider.setObjectName("zoomSlider")
        self.horizontalLayout_4.addWidget(self.zoomSlider)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.groupBox = QtWidgets.QGroupBox(fitterDialog)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stepButton = QtWidgets.QPushButton(self.groupBox)
        self.stepButton.setObjectName("stepButton")
        self.verticalLayout_3.addWidget(self.stepButton)
        self.animateButton = QtWidgets.QPushButton(self.groupBox)
        self.animateButton.setObjectName("animateButton")
        self.verticalLayout_3.addWidget(self.animateButton)
        self.fitButton = QtWidgets.QPushButton(self.groupBox)
        self.fitButton.setObjectName("fitButton")
        self.verticalLayout_3.addWidget(self.fitButton)
        self.paramsScrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.paramsScrollArea.setWidgetResizable(True)
        self.paramsScrollArea.setObjectName("paramsScrollArea")
        self.paramsScrollAreaContents = QtWidgets.QWidget()
        self.paramsScrollAreaContents.setGeometry(QtCore.QRect(0, 0, 363, 139))
        self.paramsScrollAreaContents.setObjectName("paramsScrollAreaContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.paramsScrollAreaContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.paramsScrollArea.setWidget(self.paramsScrollAreaContents)
        self.verticalLayout_3.addWidget(self.paramsScrollArea)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(fitterDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(fitterDialog)
        self.buttonBox.accepted.connect(fitterDialog.accept)
        self.buttonBox.rejected.connect(fitterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(fitterDialog)

    def retranslateUi(self, fitterDialog):
        _translate = QtCore.QCoreApplication.translate
        fitterDialog.setWindowTitle(_translate("fitterDialog", "Dialog"))
        self.openButton.setText(_translate("fitterDialog", "Open"))
        self.label.setText(_translate("fitterDialog", "Zoom"))
        self.groupBox.setTitle(_translate("fitterDialog", "Active shape model"))
        self.stepButton.setText(_translate("fitterDialog", "Step"))
        self.animateButton.setText(_translate("fitterDialog", "Animate"))
        self.fitButton.setText(_translate("fitterDialog", "Fit"))

