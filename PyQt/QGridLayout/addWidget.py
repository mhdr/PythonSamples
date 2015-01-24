from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import *


class Form(QDialog):
    def __init__(self,parent=None):
        super(Form, self).__init__(parent)

        self.label1=QLabel("Label 1")
        self.label2=QLabel("Label 2")
        self.label3=QLabel("Label 3")
        self.label4=QLabel("Label 4")

        self.grid=QGridLayout()
        self.grid.addWidget(self.label1,0,0)
        self.grid.addWidget(self.label2,0,1)
        self.grid.addWidget(self.label3,1,0)
        self.grid.addWidget(self.label4,1,1)

        self.setLayout(self.grid)

app = QApplication(sys.argv)

form=Form()
form.show()

app.exec_()

