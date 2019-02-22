from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Tables"
        self.top = 100
        self.left = 100
        self.width = 500
        self.height = 400
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.creatingTable()
        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addWidget(self.tableWidgets)
        self.setLayout(self.vBoxLayout)

        self.show()


    def creatingTable(self):

        self.tableWidgets = QTableWidget()
        self.tableWidgets.setRowCount(5)
        self.tableWidgets.setColumnCount(3)

        self.tableWidgets.setItem(0,0, QTableWidgetItem("Name"))
        self.tableWidgets.setItem(0,1, QTableWidgetItem("Email"))
        self.tableWidgets.setItem(0,2, QTableWidgetItem("Phone No"))

        self.tableWidgets.setItem(1, 0, QTableWidgetItem("Amrendra"))
        self.tableWidgets.setItem(1, 1, QTableWidgetItem("amrsanu@gmail.com"))
        self.tableWidgets.setItem(1, 2, QTableWidgetItem("+91 9140567789"))

        self.tableWidgets.setItem(2, 0, QTableWidgetItem("Ankit"))
        self.tableWidgets.setItem(2, 1, QTableWidgetItem("ankit@gmail.com"))
        self.tableWidgets.setItem(2, 2, QTableWidgetItem("+91 9457246967"))

        self.tableWidgets.setColumnWidth(1, 200)
        self.tableWidgets.setColumnWidth(2, 100)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())