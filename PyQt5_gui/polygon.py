from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen, QBrush, QPolygon
from PyQt5.QtCore import Qt, QPoint

import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Drawing Polygon"
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


    def paintEvent(self, a0: QtGui.QPaintEvent):
        painter = QPainter(self)

        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))

        points = QPolygon(
            [QPoint(10, 10),
            QPoint(10, 100),
            QPoint(100, 50),
            QPoint(100, 150)]
        )

        painter.drawPolygon(points)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())