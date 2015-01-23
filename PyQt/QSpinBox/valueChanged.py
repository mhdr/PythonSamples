from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import *


class Form(QDialog):
    def __init__(self,parent=None):
        super(Form, self).__init__(parent)
        self.spinBox=QSpinBox()
        self.spinBox.setRange(0,100)
        self.spinBox.setValue(50)

        self.spinBox.valueChanged.connect(self.print_selected)

        self.layout=QVBoxLayout()
        self.layout.addWidget(self.spinBox)
        self.setLayout(self.layout)



    def print_selected(self,value):
        current_value=self.spinBox.value()

        print(current_value)
        print(value)




app = QApplication(sys.argv)

form=Form()
form.show()

app.exec_()

