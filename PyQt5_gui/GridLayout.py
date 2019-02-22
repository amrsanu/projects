from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QMainWindow, QDialog, QGridLayout, QGroupBox, QPushButton
import sys


class Window(QDialog):

#   for the window size and icons.
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 GridLayout"
        self.top = 100
        self.left = 100
        self.width = 600
        self.height = 500
        self.setWindowIcon(QtGui.QIcon("icon.png"))

        # Calling the InitWindow to show the window
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.gridLayoutCreation()
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(self.groupbox)
        self.setLayout(vboxLayout)

        self.show()


    ### divids the window in row and columns
    def gridLayoutCreation(self):

        self.groupbox = QGroupBox("Grid Layout Example")

        gridLayout = QGridLayout()

        gridLayout.addWidget(QPushButton("1"), 0, 0)
        gridLayout.addWidget(QPushButton("2"), 0, 1)
        gridLayout.addWidget(QPushButton("3"), 0, 2)

        gridLayout.addWidget(QPushButton("4"), 1, 0)
        gridLayout.addWidget(QPushButton("5"), 1, 1)
        gridLayout.addWidget(QPushButton("6"), 1, 2)

        self.groupbox.setLayout(gridLayout)



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())