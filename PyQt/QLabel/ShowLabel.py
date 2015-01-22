import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

app=QApplication(sys.argv)

label=QLabel("<font color='red' size='72'><b>Hello World</b></font>")
label.setWindowFlags(Qt.SplashScreen)
label.show()

app.exec_()