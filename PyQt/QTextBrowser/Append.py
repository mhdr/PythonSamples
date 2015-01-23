from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

browser=QTextBrowser()

browser.append("Hello <b>Mahmood</b>")
browser.append("Hello <b>Javad</b>")

browser.show()
app.exec_()