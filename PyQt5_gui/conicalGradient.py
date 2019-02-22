from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen, QBrush, QConicalGradient
from PyQt5.QtCore import Qt, QPoint
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Drawing Linear Gradient"
        self.top = 100
        self.left = 100
        self.width = 600
        self.height = 500
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 4, Qt.SolidLine))

        conicalGradient = QConicalGradient(QPoint(100, 100), 10)
        conicalGradient.setColorAt(0.0, Qt.red)
        conicalGradient.setColorAt(0.5, Qt.green)
        conicalGradient.setColorAt(0.8, Qt.black)
        conicalGradient.setColorAt(1.0, Qt.yellow)

        painter.setBrush(QBrush(conicalGradient))

        painter.drawRect(10, 10, 200, 200)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())