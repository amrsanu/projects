from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFontDialog, QPushButton, QTextEdit, QColorDialog
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Font & Color Dialog"
        self.top = 100
        self.left = 100
        self.width = 600
        self.height = 500
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.InitWindow()

    def InitWindow(self):

        self.button = QPushButton("Open Font Dialog", self)
        self.button.setGeometry(100, 100, 100, 50)
        self.button.clicked.connect(self.createFontDialog )

        self.button2 = QPushButton("Open Color Dialog", self)
        self.button2.setGeometry(200, 100, 100, 50)
        self.button2.clicked.connect(self.createColorDialog)

        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(100, 150, 200, 200) ##(top, left, width, height)

        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def createFontDialog(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.textEdit.setFont(font)

    def createColorDialog(self):
        color = QColorDialog.getColor()
        self.textEdit.setTextColor(color)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())