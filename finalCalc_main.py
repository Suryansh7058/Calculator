from PyQt5.QtWidgets import QMainWindow

from finalCalc import *
import sys
import math
from PyQt5.QtCore import Qt, QEvent


class CalculatorApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(CalculatorApp, self).__init__(parent)
        self.setupUi(self)
        # Clear Button uses press_it method
        self.clearButton.clicked.connect(lambda: self.press_it("C"))
        # Number Buttons uses press_it method
        self.nineButton.clicked.connect(lambda: self.press_it("9"))
        self.eightButton.clicked.connect(lambda: self.press_it("8"))
        self.sevenButton.clicked.connect(lambda: self.press_it("7"))
        self.sixButton.clicked.connect(lambda: self.press_it("6"))
        self.fiveButton.clicked.connect(lambda: self.press_it("5"))
        self.fourButton.clicked.connect(lambda: self.press_it("4"))
        self.threeButton.clicked.connect(lambda: self.press_it("3"))
        self.twoButton.clicked.connect(lambda: self.press_it("2"))
        self.oneButton.clicked.connect(lambda: self.press_it("1"))
        self.zeroButton.clicked.connect(lambda: self.press_it("0"))

        # erase button
        self.eraseButton.clicked.connect(lambda: self.erase_it())
        # decimal insertion  method connection
        self.decimalButton.clicked.connect(lambda: self.dot_insert())
        # Invert plus and minus method
        self.plusminusButton.clicked.connect(lambda: self.plus_minus_invert())
        # Operator insertion method  connection
        self.divideButton.clicked.connect(lambda: self.operator_insert('/'))
        self.plusButton.clicked.connect(lambda: self.operator_insert('+'))
        self.multiplyButton.clicked.connect(lambda: self.operator_insert('*'))
        self.minusButton.clicked.connect(lambda: self.operator_insert('-'))
        self.modButton.clicked.connect(lambda: self.operator_insert('%'))

        # solve the equation method connection
        self.equalButton.clicked.connect(lambda: self.solve_it())

        # Changing cursor to Pointing Hnd when hovering over Buttons
        self.clearButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.equalButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.modButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.divideButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minusButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.multiplyButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.plusButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.eraseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nineButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.eightButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sevenButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sixButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fiveButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fourButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.threeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.twoButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.oneButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.zeroButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


    def plus_minus_invert(self):
        screen = self.outputlabel.text()
        for i in range(len(screen) - 1, -1, -1):
            if i == 0:
                if screen[i] == '-':
                    screen = screen[1:]
                    break
                else:
                    screen = '-' + screen
            else:
                if screen[i] == '+':
                    screen = screen[:i] + '-' + screen[i + 1:]
                    break
                elif screen[i] == '-':
                    screen = screen[:i] + '+' + screen[i + 1:]
                    break
        self.outputlabel.setText(screen)

    # erase last character
    def erase_it(self):
        screen = self.outputlabel.text()
        if screen == '0':
            pass
        else:
            screen = screen[:-1]
            self.outputlabel.setText(screen)

    # method to insert decimal while maintaining mathematical laws
    def dot_insert(self):
        screen = self.outputlabel.text()

        if screen[-1] == '+' or screen[-1] == '-' or screen[-1] == '*' or screen[-1] == '/' or screen[-1] == '%' \
                or screen[-1] == '.':
            return
        else:
            flag = 0
            for i in range(len(screen) - 1, -1, -1):
                if screen[i] == '+' or screen[i] == '-' or screen[i] == '/' or screen[i] == '*' or screen[i] == '%':
                    break

                elif screen[i] == '.':
                    flag += 1
                    break
                else:
                    continue

            if flag == 0:
                self.outputlabel.setText(f'{screen}.')

    # Check if valid and insert operator
    def operator_insert(self, op):
        screen = self.outputlabel.text()
        if screen[-1] == '+' or screen[-1] == '-' or screen[-1] == '*' or screen[-1] == '/' or screen[-1] == '%' \
                or screen[-1] == '.':
            pass
        else:
            self.outputlabel.setText(f'{screen}{op}')

    # Solve the Equation
    def solve_it(self):
        screen = self.outputlabel.text()
        try:
            result = eval(screen)
            if math.floor(result) == math.ceil(result):
                result = math.floor(result)
            else:
                result = "{0:.2f}".format(result)
            # display result
            self.outputlabel.setText(str(result))

        except ArithmeticError:
            self.outputlabel.setText('ERROR')

    # Method for entering number in Label and clearing label
    def press_it(self, pressed):
        if pressed == "C":
            self.outputlabel.setText("0")
        else:
            if self.outputlabel.text() == "0" or self.outputlabel.text() == 'ERROR':
                self.outputlabel.setText("")

            self.outputlabel.setText(f'{self.outputlabel.text()}{pressed}')


    def keyPressEvent(self,event):
        if event.key() == Qt.Key_0:
            self.press_it("0")
        elif event.key() == Qt.Key_1:
            self.press_it("1")
        elif event.key() == Qt.Key_2:
            self.press_it("2")
        elif event.key() == Qt.Key_3:
            self.press_it("3")
        elif event.key() == Qt.Key_4:
            self.press_it("4")
        elif event.key() == Qt.Key_5:
            self.press_it("5")
        elif event.key() == Qt.Key_6:
            self.press_it("6")
        elif event.key() == Qt.Key_7:
            self.press_it("7")
        elif event.key() == Qt.Key_8:
            self.press_it("8")
        elif event.key() == Qt.Key_9:
            self.press_it("9")
        elif event.key() == Qt.Key_Asterisk:
            self.operator_insert("*")
        elif event.key() == Qt.Key_Slash:
            self.operator_insert("/")
        elif event.key() == Qt.Key_Plus:
            self.operator_insert("+")
        elif event.key() == Qt.Key_Minus:
            self.operator_insert("-")
        elif event.key() == Qt.Key_Period:
            self.dot_insert()
        elif event.key() == Qt.Key_Equal:
            self.solve_it()
        elif event.key() == Qt.Key_Backspace:
            self.erase_it()
        elif event.key() == Qt.Key_C:
            self.press_it('C')
        elif event.key() == Qt.Key_Percent:
            self.operator_insert("%")
        elif event.key() == Qt.Key_Enter:
            self.solve_it()
        elif event.key() == Qt.Key_Escape:
            self.close()
        elif event.key() == Qt.Key_Space:
            pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # creating instance of our app
    win = CalculatorApp()

    # show and start the app
    win.show()
    app.exec_()
