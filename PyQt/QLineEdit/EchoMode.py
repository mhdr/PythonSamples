# http://doc.qt.io/qt-5/qlineedit.html#EchoMode-enum

from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import *

app=QApplication(sys.argv)

line_edit=QLineEdit()

#line_edit.setEchoMode(QLineEdit.NoEcho)
#line_edit.setEchoMode(QLineEdit.Normal)
#line_edit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
line_edit.setEchoMode(QLineEdit.Password)

line_edit.show()

app.exec_()
