import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QToolTip

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Push Button"
        self.left = 100
        self.top = 100
        self.width = 680
        self.heiht = 540
        self.setWindowIcon((QtGui.QIcon("icon.png")))

        button = QPushButton("Click Me", self)
        button.move(200, 200) # to move the button anywhere in the frame
        button.setToolTip("<h3>This is click Button</h3>") ## to give on hover tips
                            # can ues html tags. or simple string.
        # to call the window def.
        self.InitUI()


    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.heiht)
        self.show()



App = QApplication(sys.argv)

window = Window()
sys.exit(App.exec())