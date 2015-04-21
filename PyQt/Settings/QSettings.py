from PyQt5.QtCore import *
import sys

app=QCoreApplication(sys.argv)

settings=QSettings("settings.ini",QSettings.IniFormat)

settings.setValue("var1","value1")
print(settings.value("var1"))

settings.setValue("category1/var2","value2")
print(settings.value("category1/var2"))

settings.beginGroup("category2")
settings.setValue("var3","value3")
settings.setValue("var4","value4")
settings.endGroup()

app.exec_()