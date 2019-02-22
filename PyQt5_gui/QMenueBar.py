import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "QMenueBar"
        self.top = 200
        self.left = 200
        self.Widht = 600
        self.height = 500
        self.setWindowIcon(QtGui.QIcon("icon.png"))

        self.InitUI()

    def InitUI(self):

        mainMenue = self.menuBar()
        fileMenue = mainMenue.addMenu("File")
        viewMenue = mainMenue.addMenu("View")
        editMenue = mainMenue.addMenu("Edit")
        searchMenue = mainMenue.addMenu("Search")
        toolMenue = mainMenue.addMenu("Tool")
        helpMenue = mainMenue.addMenu("Help")

        exitButton = QAction(QIcon("exit.png"), 'Exit', self)
        exitButton.setShortcut("Ctrl+E")
        exitButton.setStatusTip("ExitApplication")
        exitButton.triggered.connect(self.close)

        fileMenue.addAction(exitButton)



        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width(), self.height)
        self.show()

App = QApplication(sys.argv)

window = Window()
sys.exit(App.exec())