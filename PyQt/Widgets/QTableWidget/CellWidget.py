from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import *


class Form(QWidget):
    def __init__(self,parent=None):
        super(Form, self).__init__(parent)

        self.table=QTableWidget()
        self.table.setColumnCount(2)
        self.table.setRowCount(2)

        item1=QComboBox()

        item2=QLabel("Item2")

        item3=QPushButton("Item3")

        item4=QProgressBar()

        self.table.setCellWidget(0,0,item1)
        self.table.setCellWidget(0,1,item2)
        self.table.setCellWidget(1,0,item3)
        self.table.setCellWidget(1,1,item4)

        headers=["First Name","Last Name"]
        self.table.setHorizontalHeaderLabels(headers)

        layout=QFormLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)

app = QApplication(sys.argv)

form=Form()
form.show()

app.exec_()
