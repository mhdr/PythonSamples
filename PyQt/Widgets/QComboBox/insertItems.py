from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)


data=["Mahmood","Majeed","Javad","Mohsen","Hamid","Rashid","Ali"]
comboBox=QComboBox()
comboBox.insertItems(0,data)
comboBox.setFixedWidth(200)
comboBox.show()

app.exec_()