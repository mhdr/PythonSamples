from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

browser=QTextBrowser()

browser.setHtml("Hello <b>Mahmood</b>")
browser.setHtml("Hello <b>Javad</b>")

browser.show()
app.exec_()