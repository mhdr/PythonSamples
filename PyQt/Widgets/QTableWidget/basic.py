from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import *


class Form(QWidget):
    def __init__(self,parent=None):
        super(Form, self).__init__(parent)

        self.table=QTableWidget()
        self.table.setColumnCount(2)
        self.table.setRowCount(2)

        item1=QTableWidgetItem()
        item1.setText("item1")

        item2=QTableWidgetItem()
        item2.setText("item2")

        item3=QTableWidgetItem()
        item3.setText("item3")

        item4=QTableWidgetItem()
        item4.setText("item4")

        self.table.setItem(0,0,item1)
        self.table.setItem(0,1,item2)
        self.table.setItem(1,0,item3)
        self.table.setItem(1,1,item4)

        headers=["First Name","Last Name"]
        self.table.setHorizontalHeaderLabels(headers)

        layout=QFormLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)

app = QApplication(sys.argv)

form=Form()
form.show()

app.exec_()
