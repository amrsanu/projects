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

        button = QPushButton("About Box", self)
        button.move(200, 200)
        button.clicked.connect(self.AboutMessage)

        button2 = QPushButton("Question Message", self)
        button2.move(100, 100)
        button2.clicked.connect(self.QuestionMessage)

        self.InitUI()

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.heiht)
        self.show()

    def AboutMessage(self):
        QMessageBox.about(self, "About Message", "This is about message box, from youtube.")

    def QuestionMessage(self):
        message = QMessageBox.question(self, "Question Message", "Have you subscribed my channel.", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if(message == QMessageBox.Yes):
            print("Yes I have subscribed")
        else:
            print("No I have not subscribed.")
App = QApplication(sys.argv)

window = Window()
sys.exit(App.exec())