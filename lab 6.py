import sys
import re
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox

class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_second = QHBoxLayout()
        self.hbox_third = QHBoxLayout()
        self.hbox_result = QHBoxLayout()

        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_second)
        self.vbox.addLayout(self.hbox_third)
        self.vbox.addLayout(self.hbox_result)
        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        self.b_0 = QPushButton("0", self)
        self.hbox_first.addWidget(self.b_0)

        self.b_1 = QPushButton("1", self)
        self.hbox_first.addWidget(self.b_1)

        self.b_2 = QPushButton("2", self)
        self.hbox_first.addWidget(self.b_2)

        self.b_3 = QPushButton("3", self)
        self.hbox_first.addWidget(self.b_3)

        self.b_4 = QPushButton("4", self)
        self.hbox_second.addWidget(self.b_4)

        self.b_5 = QPushButton("5", self)
        self.hbox_second.addWidget(self.b_5)

        self.b_6 = QPushButton("6", self)
        self.hbox_second.addWidget(self.b_6)

        self.b_7 = QPushButton("7", self)
        self.hbox_second.addWidget(self.b_7)

        self.b_8 = QPushButton("8", self)
        self.hbox_third.addWidget(self.b_8)

        self.b_9 = QPushButton("9", self)
        self.hbox_third.addWidget(self.b_9)

        self.b_plus = QPushButton("+", self)
        self.hbox_first.addWidget(self.b_plus)

        self.b_sub = QPushButton("-", self)
        self.hbox_second.addWidget(self.b_sub)

        self.b_mult = QPushButton("*", self)
        self.hbox_third.addWidget(self.b_mult)

        self.b_div = QPushButton("/", self)
        self.hbox_third.addWidget(self.b_div)

        self.b_point = QPushButton(".", self)
        self.hbox_third.addWidget(self.b_point)

        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)

        self.b_reset = QPushButton("<-", self)
        self.hbox_result.addWidget(self.b_reset)
        self.b_hard_reset = QPushButton("c", self)
        self.hbox_result.addWidget(self.b_hard_reset)

        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_sub.clicked.connect(lambda: self._operation("-"))
        self.b_mult.clicked.connect(lambda: self._operation("*"))
        self.b_div.clicked.connect(lambda: self._operation("/"))
        self.b_result.clicked.connect(self._result)
        self.b_reset.clicked.connect(self._reset)
        self.b_hard_reset.clicked.connect(self._hard_reset)

        self.b_0.clicked.connect(lambda: self._button("0"))
        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_point.clicked.connect(lambda: self._button("."))

    def _button(self, param):
            line = self.input.text()
            self.input.setText(line + param)

    def _reset(self):
        self.input.setText("")

    def _hard_reset(self):
        self.num_1 = 0
        self.input.setText("")

    def _operation(self, op):
        if self.input.text() == "":
            return
        elif re.findall(r'\D', self.input.text()) and (len(re.findall(r'\.', self.input.text())) >= 2 or re.findall(r'\.', self.input.text()) == []):
            QMessageBox.about(self, "Error", "неправильный ввод")
            self.input.setText("")
        else:
            self.num_1 = float(self.input.text())
            self.op = op
            self.input.setText("")
            self.k = 0

    def _result(self):

            if self.input.text() == "":
                return
            elif re.findall(r'\D', self.input.text()) and (len(re.findall(r'\.', self.input.text())) >= 2 or re.findall(r'\.', self.input.text()) == []):
                QMessageBox.about(self, "Error", "неправильный ввод")
                self.input.setText("")
            else:
                self.num_2 = float(self.input.text())
                try:
                    if self.op == "+":
                        self.input.setText(str(self.num_1 + self.num_2))
                    if self.op == "-":
                        self.input.setText(str(self.num_1 - self.num_2))
                    if self.op == "*":
                        self.input.setText(str(self.num_1 * self.num_2))
                    if self.op == "/":
                        if self.num_2 == 0:
                            QMessageBox.about(self, "Error", "Деление на ноль")
                            self.input.setText("")
                        else:
                            self.input.setText(str(self.num_1 / self.num_2))
                except BaseException:
                    return
                if self.k == 0:
                    self.num_1 = self.num_2
                    self.k = 1


app = QApplication(sys.argv)

win = Calculator()
win.show()

sys.exit(app.exec_())