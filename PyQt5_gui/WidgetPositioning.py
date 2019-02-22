from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys


class Window(QMainWindow):

#   for the window size and icons.
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Widget Positioning"
        self.top = 100
        self.left = 100
        self.width = 600
        self.height = 500
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.InitWindow()

    def InitWindow(self):


        ### can move any widget by using this method
        self.label1 = QLabel("Please", self)
        self.label1.move(50, 50)

        self.label2 = QLabel("Subscribe", self)
        self.label2.move(100, 100)

        self.label3 = QLabel("My", self)
        self.label3.move(150, 150)

        self.label4 = QLabel("Channel", self)
        self.label4.move(200, 200)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())