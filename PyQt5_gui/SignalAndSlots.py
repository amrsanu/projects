import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QPushButton, QToolTip
from PyQt5.QtCore import QCoreApplication

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Push Button"
        self.left = 100
        self.top = 100
        self.width = 680
        self.heiht = 540
        self.setWindowIcon((QtGui.QIcon("icon.png")))

        button = QPushButton("Close", self)
        button.move(200, 200) # to move the button anywhere in the frame
        button.setToolTip("<h3>This is close Button</h3>") ## to give on hover tips# can ues html tags. or simple string.

        button.clicked.connect(self.CloseApp)
        self.InitUI()


    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.heiht)
        self.show()

    def CloseApp(self):
        reply = QMessageBox.question(self, "Close Meassage", "Areyou sure to close window?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.close()


App = QApplication(sys.argv)

window = Window()
sys.exit(App.exec())