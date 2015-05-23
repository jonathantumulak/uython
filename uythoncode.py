import sys
import os
from PyQt4 import QtCore, QtGui
import uython
from myHL import MyHL

class UythonWindow(QtGui.QMainWindow, uython.Ui_Uython):
    def __init__(self, parent=None):
        super(UythonWindow, self).__init__(parent)
        self.setupUi(self)
        self.compiler = MyHL()
        self.executeBtn.clicked.connect(self.executeCode)
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionSave_As.triggered.connect(self.save_as_file)
        self.editorTxtEdit.viewport().installEventFilter(QEditorDropHandler(self, self.editorTxtEdit))
        self.format = QtGui.QTextBlockFormat()
        self.format.setBackground(QtCore.Qt.yellow)
        self.clearformat = QtGui.QTextBlockFormat()

        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)

    def __del__(self):
        sys.stdout = sys.__stdout__

    def normalOutputWritten(self, text):
        cursor = self.consoleTxtEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.consoleTxtEdit.setTextCursor(cursor)
        self.consoleTxtEdit.ensureCursorVisible()

    def executeCode(self):
        self.consoleTxtEdit.clear()
        self.clearlineformat()
        code = self.editorTxtEdit.toPlainText()
        if code:
            code = unicode(code)
            code = code.encode('utf_8')
            code = code.split('\n')
            self.compiler.run(code, self)
        else:
            print "empty"

    def open_file(self):
        self.editorTxtEdit.clear()
        openfile = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '', 'Uython Files (*.uy)')
        if openfile:
            self.currentfile = openfile
            f = open(openfile, 'r')
            self.editorTxtEdit.setText(f.read())
            f.close()

    def save_as_file(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '', 'Uython Files (*.uy)')
        if filename:
            self.currentfile = filename
            fname = open(filename, 'w')
            fname.write(self.editorTxtEdit.toPlainText())
            fname.close()

    def save_file(self):
        if self.currentfile:
            os.remove(str(self.currentfile))
            f = open(self.currentfile, 'w') # New line
            f.write(self.editorTxtEdit.toPlainText())
            f.close()

    def getInt(self, var):
        return QtGui.QInputDialog.getInt(self, 'Input Dialog', "Enter value for variable %s:" % var)

    def getString(self, var):
        return QtGui.QInputDialog.getText(self, 'Input Dialog', "Enter value for variable %s:" % var)

    def clearlineformat(self):
        code = self.editorTxtEdit.toPlainText()
        code = code.split('\n')
        for x in range(0, len(code)):
            cursor = QtGui.QTextCursor(self.editorTxtEdit.document().findBlockByNumber(x))
            cursor.setBlockFormat(self.clearformat)

    def setLineFormat(self, lineNumber):
        cursor = QtGui.QTextCursor(self.editorTxtEdit.document().findBlockByNumber(lineNumber))
        cursor.setBlockFormat(self.format)

class QEditorDropHandler(QtCore.QObject):
    def __init__(self, parent=None, *args, **kwargs):
        QtCore.QObject.__init__(self, parent)
        self.initcode(*args, **kwargs)

    def initcode(self, asmtextedit):
        self.asmtextedit = asmtextedit

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.DragEnter:
            data = event.mimeData()
            urls = data.urls()
            if (urls and urls[0].scheme() == 'file'):
                event.accept()
                return True

        if event.type() == QtCore.QEvent.DragMove:
            data = event.mimeData()
            urls = data.urls()
            if (urls and urls[0].scheme() == 'file'):
                event.accept()
                return True

        if event.type() == QtCore.QEvent.Drop:
            data = event.mimeData()
            urls = data.urls()
            if (urls and urls[0].scheme() == 'file'):
                # for some reason, this doubles up the intro slash
                # filepath = urls[0].toString()
                path = urls[0].toLocalFile().toLocal8Bit().data()
                if os.path.isfile(path):
                    print path
                    f = open(path, 'r')
                    lines = f.read()
                    self.asmtextedit.setText(lines)
                else:
                    print "Not a file"
                return True
        return False



class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

app = QtGui.QApplication(sys.argv)
form = UythonWindow()
form.show()
app.exec_()