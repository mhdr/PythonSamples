from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)


comboBox=QComboBox()

comboBox.insertItem(0,"Mahmood")
comboBox.insertItem(0,"Javad")
comboBox.insertItem(0,"Ali")

count=comboBox.count()
comboBox.insertItem(count,"Hamid")

comboBox.setFixedWidth(200)
comboBox.show()

app.exec_()