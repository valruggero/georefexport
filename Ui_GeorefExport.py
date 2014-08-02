# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_GeorefExport.ui'
#
# Created: Mon Jul 21 23:09:23 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_GeorefExport(object):
    def setupUi(self, GeorefExport):
        GeorefExport.setObjectName(_fromUtf8("GeorefExport"))
        GeorefExport.resize(504, 649)
        self.groupBox_2 = QtGui.QGroupBox(GeorefExport)
        self.groupBox_2.setGeometry(QtCore.QRect(9, 260, 481, 381))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(2, 80, 471, 231))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.textEdit = QtGui.QTextEdit(self.groupBox_3)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 451, 181))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.layoutWidget = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(13, 20, 461, 54))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)
        self.btnOutputFile = QtGui.QToolButton(self.layoutWidget)
        self.btnOutputFile.setMinimumSize(QtCore.QSize(0, 25))
        self.btnOutputFile.setMaximumSize(QtCore.QSize(16777215, 25))
        self.btnOutputFile.setObjectName(_fromUtf8("btnOutputFile"))
        self.gridLayout_2.addWidget(self.btnOutputFile, 0, 0, 1, 1)
        self.lineOutput = QtGui.QLineEdit(self.layoutWidget)
        self.lineOutput.setMinimumSize(QtCore.QSize(280, 25))
        self.lineOutput.setMaximumSize(QtCore.QSize(280, 25))
        self.lineOutput.setObjectName(_fromUtf8("lineOutput"))
        self.gridLayout_2.addWidget(self.lineOutput, 0, 1, 1, 1)
        self.checkAddRes = QtGui.QCheckBox(self.layoutWidget)
        self.checkAddRes.setEnabled(True)
        self.checkAddRes.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkAddRes.setText(_fromUtf8(""))
        self.checkAddRes.setObjectName(_fromUtf8("checkAddRes"))
        self.gridLayout_2.addWidget(self.checkAddRes, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(GeorefExport)
        self.buttonBox.setGeometry(QtCore.QRect(195, 610, 271, 27))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.groupBox = QtGui.QGroupBox(GeorefExport)
        self.groupBox.setGeometry(QtCore.QRect(9, 30, 481, 231))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.gridLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.lblFlowDir = QtGui.QLabel(self.groupBox)
        self.lblFlowDir.setMaximumSize(QtCore.QSize(100, 20))
        self.lblFlowDir.setObjectName(_fromUtf8("lblFlowDir"))
        self.gridLayout_3.addWidget(self.lblFlowDir, 2, 0, 1, 1)
        self.lblDpi = QtGui.QLabel(self.groupBox)
        self.lblDpi.setMaximumSize(QtCore.QSize(100, 20))
        self.lblDpi.setAutoFillBackground(False)
        self.lblDpi.setMargin(1)
        self.lblDpi.setObjectName(_fromUtf8("lblDpi"))
        self.gridLayout_3.addWidget(self.lblDpi, 1, 0, 1, 1)
        self.spinBoxWidth = QtGui.QSpinBox(self.groupBox)
        self.spinBoxWidth.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBoxWidth.setMinimum(100)
        self.spinBoxWidth.setMaximum(100000)
        self.spinBoxWidth.setSingleStep(10)
        self.spinBoxWidth.setProperty("value", 2000)
        self.spinBoxWidth.setObjectName(_fromUtf8("spinBoxWidth"))
        self.gridLayout_3.addWidget(self.spinBoxWidth, 2, 1, 1, 1)
        self.spinBoxDpi = QtGui.QSpinBox(self.groupBox)
        self.spinBoxDpi.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBoxDpi.setMinimum(10)
        self.spinBoxDpi.setMaximum(2000)
        self.spinBoxDpi.setProperty("value", 96)
        self.spinBoxDpi.setObjectName(_fromUtf8("spinBoxDpi"))
        self.gridLayout_3.addWidget(self.spinBoxDpi, 1, 1, 1, 1)
        self.lineEditSourceSrs = QtGui.QLineEdit(self.groupBox)
        self.lineEditSourceSrs.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEditSourceSrs.setCursorPosition(5)
        self.lineEditSourceSrs.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditSourceSrs.setObjectName(_fromUtf8("lineEditSourceSrs"))
        self.gridLayout_3.addWidget(self.lineEditSourceSrs, 0, 1, 1, 1)
        self.lbl_ProjectSrs = QtGui.QLabel(self.groupBox)
        self.lbl_ProjectSrs.setMaximumSize(QtCore.QSize(100, 20))
        self.lbl_ProjectSrs.setAutoFillBackground(False)
        self.lbl_ProjectSrs.setMargin(1)
        self.lbl_ProjectSrs.setObjectName(_fromUtf8("lbl_ProjectSrs"))
        self.gridLayout_3.addWidget(self.lbl_ProjectSrs, 0, 0, 1, 1)
        self.cmboxImgFormat = QtGui.QComboBox(self.groupBox)
        self.cmboxImgFormat.setObjectName(_fromUtf8("cmboxImgFormat"))
        self.gridLayout_3.addWidget(self.cmboxImgFormat, 3, 1, 1, 1)
        self.lblImgFormat = QtGui.QLabel(self.groupBox)
        self.lblImgFormat.setMaximumSize(QtCore.QSize(100, 20))
        self.lblImgFormat.setObjectName(_fromUtf8("lblImgFormat"))
        self.gridLayout_3.addWidget(self.lblImgFormat, 3, 0, 1, 1)
        self.lblImgFormat_2 = QtGui.QLabel(self.groupBox)
        self.lblImgFormat_2.setMaximumSize(QtCore.QSize(100, 20))
        self.lblImgFormat_2.setObjectName(_fromUtf8("lblImgFormat_2"))
        self.gridLayout_3.addWidget(self.lblImgFormat_2, 4, 0, 1, 1)
        self.checkWFile = QtGui.QCheckBox(self.groupBox)
        self.checkWFile.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkWFile.setText(_fromUtf8(""))
        self.checkWFile.setChecked(False)
        self.checkWFile.setObjectName(_fromUtf8("checkWFile"))
        self.gridLayout_3.addWidget(self.checkWFile, 4, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.label = QtGui.QLabel(GeorefExport)
        self.label.setGeometry(QtCore.QRect(60, 10, 411, 17))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(GeorefExport)
        QtCore.QMetaObject.connectSlotsByName(GeorefExport)
        GeorefExport.setTabOrder(self.lineEditSourceSrs, self.spinBoxDpi)
        GeorefExport.setTabOrder(self.spinBoxDpi, self.spinBoxWidth)
        GeorefExport.setTabOrder(self.spinBoxWidth, self.btnOutputFile)
        GeorefExport.setTabOrder(self.btnOutputFile, self.lineOutput)
        GeorefExport.setTabOrder(self.lineOutput, self.buttonBox)
        GeorefExport.setTabOrder(self.buttonBox, self.textEdit)

    def retranslateUi(self, GeorefExport):
        GeorefExport.setWindowTitle(QtGui.QApplication.translate("GeorefExport", "GeorefExport", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("GeorefExport", "Output ", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("GeorefExport", "Log", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("GeorefExport", "Add result to project", None, QtGui.QApplication.UnicodeUTF8))
        self.btnOutputFile.setText(QtGui.QApplication.translate("GeorefExport", "Output File...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("GeorefExport", "Input ", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFlowDir.setText(QtGui.QApplication.translate("GeorefExport", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">WIDTH [pixel]:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDpi.setText(QtGui.QApplication.translate("GeorefExport", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">DPI:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditSourceSrs.setText(QtGui.QApplication.translate("GeorefExport", "25832", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_ProjectSrs.setText(QtGui.QApplication.translate("GeorefExport", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Project CRS:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblImgFormat.setText(QtGui.QApplication.translate("GeorefExport", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Image format:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblImgFormat_2.setText(QtGui.QApplication.translate("GeorefExport", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Worldfile</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("GeorefExport", "Exports the map as a georeferenced raster graphics file.", None, QtGui.QApplication.UnicodeUTF8))

