from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

msgBox=QMessageBox()
msgBox.setText("Hello World")
msgBox.exec_()

app.exec_()