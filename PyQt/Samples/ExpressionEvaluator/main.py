from PyQt5.QtCore import *
import sys
from math import *
from PyQt5.QtWidgets import *


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.browser = QTextBrowser()
        self.line_edit = QLineEdit("Enter your expression.")

        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.line_edit)
        self.setLayout(layout)

        self.line_edit.selectAll()
        self.line_edit.setFocus()

        self.line_edit.returnPressed.connect(self.update_ui)
        self.setWindowTitle("Calculate")


    def update_ui(self):
        text = self.line_edit.text()

        try:
            result = eval(text)
            self.browser.append("<b>{0} = </b>{1}".format(text, result))
            self.line_edit.setText("")
        except:
            self.browser.append("<font color='red'><b>{0} : </b>Invalid</font>".format(text))


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()