from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction
from PyQt5.QtCore import Qt
import sys


class DisplayWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("First Qt application")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("My first label in \nthe First\nApplication")
        self.label.adjustSize()
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click Me")
        self.b1.clicked.connect(self.clickedButton)

    def clickedButton(self):
        self.label.setText("You clicked the button")
        self.update()

    def update(self):
        self.label.adjustSize()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            print("Space Bar Pressed")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # creating instance of our app
    ui = DisplayWindow()
    # show and start the app
    ui.show()
    app.exec_()
