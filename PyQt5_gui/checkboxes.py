from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox
import sys
from PyQt5.QtCore import Qt


class Window(QMainWindow):

#   for the window size and icons.
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 CheckBoxes"
        self.top = 100
        self.left = 100
        self.width = 600
        self.height = 500
        self.setWindowIcon(QtGui.QIcon("save.png"))

        # Calling the InitWindow to show the window
        self.InitWindow()

    def InitWindow(self):

        checkBox = QCheckBox("Do you like Football?", self)
        checkBox.move(100, 100)
        checkBox.toggle()  # To show already checked

        checkBox.stateChanged.connect(self.checkBoxChanged)

        ### textLabel of the checkbox
        self.label = QLabel("Hello", self)
        self.label.move(100, 150)

        self.setWindowIcon(QtGui.QIcon("save.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def checkBoxChanged(self, state):
        if state == Qt.Checked:
            self.label.setText("Yes I like Football")
        else:
            self.label.setText("No I don't Football")

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())