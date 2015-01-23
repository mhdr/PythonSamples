from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

msgBox=QMessageBox()
msgBox.setText("The document has been modified")
msgBox.setInformativeText("Do you want to save you changes?")
msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel | QMessageBox.Discard)
msgBox.setDefaultButton(QMessageBox.Save)

result=msgBox.exec_()

if result==QMessageBox.Save:
    print("Save")
elif result==QMessageBox.Cancel:
    print("Cancel")
elif result==QMessageBox.Discard:
    print("Discard")

app.exec_()