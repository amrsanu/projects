from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QSlider, QWidget
import sys
from PyQt5.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Slider Part 2"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.InitWindow()

    def InitWindow(self):

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setGeometry(60, 60, 150, 20)
        self.slider.valueChanged[int].connect(self.changedValue)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("save.png"))
        self.label.setGeometry(60, 100, 150, 120)

        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()


    def changedValue(self, value):
        if value == 0:
            self.label.setPixmap(QPixmap("save.jpg"))
        elif value < 50:
            self.label.setPixmap(QPixmap("exit.png"))
        else:
            self.label.setPixmap(QPixmap("Paste.png"))

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())