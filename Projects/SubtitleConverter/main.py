#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from main_widget import MainWidget

app = QApplication(sys.argv)

# set icon for application
window_icon=QIcon("./resources/srt.ico")
if not window_icon.isNull():
    app.setWindowIcon(window_icon)

form=MainWidget()
form.show()

app.exec_()