import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QApplication

app=QApplication(sys.argv)

engine=QQmlApplicationEngine()
engine.load(QUrl("qrc:/main.qml"))

app.exec_()