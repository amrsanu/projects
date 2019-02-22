from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QBrush, QPainter, QPen
from PyQt5.QtCore import Qt
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Brush Styles"
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

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setPen(QPen(Qt.blue, 4, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.DiagCrossPattern))
        painter.drawRect(10, 100, 150, 100)

        painter.setPen(QPen(Qt.blue, 4, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.Dense1Pattern))
        painter.drawRect(100, 150, 150, 100)

        painter.setPen(QPen(Qt.blue, 4, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.HorPattern))
        painter.drawRect(180, 100, 150, 100)

        painter.setPen(QPen(Qt.blue, 4, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.VerPattern))
        painter.drawRect(180, 220, 150, 100)

        painter.setPen(QPen(Qt.blue, 4, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.BDiagPattern))
        painter.drawRect(10, 220, 150, 100)

        painter.setPen(QPen(Qt.blue, 4, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.Dense3Pattern))
        painter.drawRect(350, 100, 150, 100)
        painter.setPen(QPen(Qt.blue, 4, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.Dense6Pattern))
        painter.drawRect(350, 220, 150, 100)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())