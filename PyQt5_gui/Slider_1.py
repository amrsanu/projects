from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QMainWindow, QSlider, QWidget, QLineEdit
import sys
from PyQt5.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Slider Part1"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 200
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.InitWindow()

    def InitWindow(self):

        vboxLayout = QVBoxLayout()
        self.lineEdit = QLineEdit(self)
        vboxLayout.addWidget(self.lineEdit)
        self.lineEdit.move(100, 50)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.move(100, 20)
        self.slider.setMinimum(1)
        self.slider.setMaximum(99)
        self.slider.setValue(20)   #    default value = 0, (to set the initial value)

        ###     to show the ticks
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(10)

        self.slider.valueChanged.connect(self.changedValue)
        vboxLayout.addWidget(self.slider)

        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()


    def changedValue(self):
        size = str(self.slider.value())
        self.lineEdit.setText(size)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())