# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uython.ui'
#
# Created: Sat May 23 23:34:02 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Uython(object):
    def setupUi(self, Uython):
        Uython.setObjectName(_fromUtf8("Uython"))
        Uython.resize(800, 598)
        Uython.setStyleSheet(_fromUtf8(" background-color: rgb(33, 88, 215);"))
        self.centralwidget = QtGui.QWidget(Uython)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.editorTxtEdit = QtGui.QTextEdit(self.centralwidget)
        self.editorTxtEdit.setGeometry(QtCore.QRect(20, 10, 581, 371))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(143, 167, 228))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(143, 167, 228))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(143, 167, 228))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(143, 167, 228))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(143, 167, 228))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(143, 167, 228))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(143, 167, 228))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(143, 167, 228))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(143, 167, 228))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.editorTxtEdit.setPalette(palette)
        self.editorTxtEdit.setStyleSheet(_fromUtf8(" background-color: rgb(143, 167, 228);"))
        self.editorTxtEdit.setObjectName(_fromUtf8("editorTxtEdit"))
        self.consoleTxtEdit = QtGui.QTextEdit(self.centralwidget)
        self.consoleTxtEdit.setGeometry(QtCore.QRect(20, 410, 761, 151))
        self.consoleTxtEdit.setStyleSheet(_fromUtf8(" background-color: rgb(143, 167, 228);"))
        self.consoleTxtEdit.setObjectName(_fromUtf8("consoleTxtEdit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 390, 61, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.executeBtn = QtGui.QPushButton(self.centralwidget)
        self.executeBtn.setGeometry(QtCore.QRect(620, 350, 161, 31))
        self.executeBtn.setStyleSheet(_fromUtf8("background-color: rgb(255, 237, 148)"))
        self.executeBtn.setObjectName(_fromUtf8("executeBtn"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(620, 10, 161, 201))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/teser.jpg")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        Uython.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Uython)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        Uython.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Uython)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Uython.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(Uython)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(Uython)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionAbout = QtGui.QAction(Uython)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionSave_As = QtGui.QAction(Uython)
        self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Uython)
        QtCore.QMetaObject.connectSlotsByName(Uython)

    def retranslateUi(self, Uython):
        Uython.setWindowTitle(_translate("Uython", "Uython", None))
        self.label.setText(_translate("Uython", "Console", None))
        self.executeBtn.setText(_translate("Uython", "Execute", None))
        self.menuFile.setTitle(_translate("Uython", "File", None))
        self.menuHelp.setTitle(_translate("Uython", "Help", None))
        self.actionOpen.setText(_translate("Uython", "Open", None))
        self.actionSave.setText(_translate("Uython", "Save", None))
        self.actionAbout.setText(_translate("Uython", "About", None))
        self.actionSave_As.setText(_translate("Uython", "Save As...", None))

import uythonresource_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Uython = QtGui.QMainWindow()
    ui = Ui_Uython()
    ui.setupUi(Uython)
    Uython.show()
    sys.exit(app.exec_())

