from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout, QGroupBox
import sys

## In place of QmainWindow we are using QDialog
class Window(QDialog):

#   for the window size and icons.
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Layouts"
        self.top = 100
        self.left = 100
        self.width = 300
        self.height = 100
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.HorizontalLayout()

        vBox = QVBoxLayout()
        vBox.addWidget(self.groupBox)
        self.setLayout(vBox)

        self.show()

    def HorizontalLayout(self):
        self.groupBox = QGroupBox("What is Your Favourite Sport??")
        hBoxLayout = QHBoxLayout()

        button1 = QPushButton("Football", self)
        button1.clicked.connect(self.button1Clicked)
        hBoxLayout.addWidget(button1)

        button2 = QPushButton("Cricket", self)
        button2.clicked.connect(self.button2Clicked)
        hBoxLayout.addWidget(button2)

        button3 = QPushButton("Tennis", self)
        button3.clicked.connect(self.button3Clicked)
        hBoxLayout.addWidget(button3)

        self.groupBox.setLayout(hBoxLayout)

    def button1Clicked(self):
        QMessageBox.information(self, "Football", "Yes I Like Football")

    def button2Clicked(self):
        QMessageBox.information(self, "Cricket", "Yes I Like Cricket")

    def button3Clicked(self):
        QMessageBox.information(self, "Tennis", "Yes I Like Tennis")

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())