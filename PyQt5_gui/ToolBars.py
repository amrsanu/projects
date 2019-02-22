from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
import sys


class Window(QMainWindow):

#   for the window size and icons.
    def __init__(self):
        super().__init__()

        self.title = "ToolBars"
        self.top = 100
        self.left = 100
        self.width = 600
        self.height = 500
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.InitWindow()

    def InitWindow(self):

        exitAct = QAction(QIcon("exit.png"), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        # To exit give triggered action
        exitAct.triggered.connect(self.CloseApp)

        copyAct = QAction(QIcon('copy.png'), "copy", self)
        copyAct.setShortcut("Ctrl+C")

        pasteAct = QAction(QIcon("paste.png"), "paste", self)
        pasteAct.setShortcut("Ctrl+V")

        deleteAct = QAction(QIcon("delete.png"), "Delete", self)
        deleteAct.setShortcut("Ctrl+D")

        saveAct = QAction(QIcon("save.png"), "Save", self)
        saveAct.setShortcut("Ctrl+S")

        self.toolbar = self.addToolBar("Toolbar")
        self.toolbar.addAction(exitAct)
        self.toolbar.addAction(copyAct)
        self.toolbar.addAction(pasteAct)
        self.toolbar.addAction(saveAct)
        self.toolbar.addAction(deleteAct)


        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def CloseApp(self):
        self.close()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())