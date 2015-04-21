from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import *


class Form(QDialog):
    def __init__(self,parent=None):
        super(Form, self).__init__(parent)
        data = ["Mahmood", "Majeed", "Javad", "Mohsen", "Hamid", "Rashid", "Ali"]

        self.comboBox = QComboBox()
        self.comboBox.insertItems(0, data)
        self.comboBox.setFixedWidth(200)

        # select nothing
        self.comboBox.setCurrentIndex(-1)

        # is always emitted regardless if the change was done programmatically or by user interaction
        self.comboBox.activated.connect(self.print_selected)

        self.layout=QVBoxLayout()
        self.layout.addWidget(self.comboBox)
        self.setLayout(self.layout)


    def print_selected(self,index):
        # get current text
        # current_text = self.comboBox.currentText()
        current_item=self.comboBox.itemText(index)

        # change an item
        self.comboBox.removeItem(index)

        output="{0} : {1}".format(index,current_item)
        print(output)

app = QApplication(sys.argv)

form=Form()
form.show()

app.exec_()


