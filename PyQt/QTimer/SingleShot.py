from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

def print_time():
    print(QTime.currentTime().toPyTime())

app=QGuiApplication(sys.argv)

# the event fires just one time
QTimer.singleShot(2000,print_time)

app.exec_()

