from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QSpinBox, QLabel, QVBoxLayout, QDoubleSpinBox
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 SpinBox"

        #Initial location of thr window
        self.top = 900
        self.left = 100
        ## size of the window
        self.width = 300
        self.height = 200
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.InitWindow()

    def InitWindow(self):

        vBoxLayout = QVBoxLayout()
        self.label = QLabel("Current value: ", self)
        self.label.move(60, 60)
        vBoxLayout.addWidget(self.label)

        self.spinBox = QDoubleSpinBox(self)
        self.spinBox.move(60, 35)
        self.spinBox.setMinimum(10.00) #to give the initial value  (wii be th mininum)
        self.spinBox.setMaximum(20.00) # to give the upper limit
        self.spinBox.valueChanged.connect(self.valueChanged)
        vBoxLayout.addWidget(self.spinBox)

        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()


    def valueChanged(self):
        self.label.setText("Current Value: " + str(self.spinBox.value()))


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())