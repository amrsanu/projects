import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QStatusBar, QMenu, QMenuBar, QAction


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "QStatus Bar"
        self.top = 200
        self.left = 200
        self.Widht = 600
        self.height = 500
        self.setWindowIcon(QtGui.QIcon("icon.png"))

        self.InitUI()

    def InitUI(self):

        self.statusbar = self.statusBar()
        self.statusbar.showMessage("Message is ready")

        menuebar = self.menuBar()
        viewMenue = menuebar.addMenu("View")

        viewAction = QAction("View Status", self, checkable = True)
        viewAction.setStatusTip("View StatusBar")
        viewAction.setChecked(True)
        viewAction.triggered.connect(self.toggleMenue)

        viewMenue.addAction(viewAction)

        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width(), self.height)
        self.show()


    def toggleMenue(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

App = QApplication(sys.argv)

window = Window()
sys.exit(App.exec())