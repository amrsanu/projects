from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QFileDialog
from PyQt5.QtCore import QFileInfo
from PyQt5.QtPrintSupport import QPrinter
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 PDF from Text (PDF Exporter)"
        self.top = 100
        self.left = 100
        self.width = 600
        self.height = 500
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.InitWindow()

    def InitWindow(self):

        self.button = QPushButton("Export PDF", self)
        self.button.setGeometry(100, 100, 100, 50)
        self.button.clicked.connect(self.printPDF)

        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(100, 150, 400, 400)

        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def printPDF(self):
        fn, _ = QFileDialog.getSaveFileName(self, 'Export PDF', None, 'PDF files (.pdf);;All Files')

        if fn != '':
            if QFileInfo(fn).suffix() ==  "":
                fn += '.pdf'

            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            self.textEdit.document().print_(printer)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())