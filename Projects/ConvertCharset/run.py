#!/usr/bin/python3

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from Converter import Converter

ASSERT=False

class Form(QWidget):
    def __init__(self,parent=None):
        super(Form, self).__init__(parent)

        # initialize settings
        self.settings=QSettings("settings.ini",QSettings.IniFormat)

        # initialize UI
        self.setMinimumHeight(125)
        self.setWindowTitle("Subtitle Converter")

        self.label=QLabel("File")

        self.lineEdit=QLineEdit()
        self.lineEdit.setFixedWidth(600)
        self.lineEdit.setReadOnly(True)

        self.button_browse=QPushButton("Browse...")
        self.button_browse.clicked.connect(self.button_browse_clicked)

        self.button_convert=QPushButton("Convert")
        self.button_convert.clicked.connect(self.button_convert_clicked)

        self.layout=QHBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.button_browse)
        self.layout.addWidget(self.button_convert)

        self.setLayout(self.layout)

        # restore geometry
        mainWidgetGeometry= self.settings.value("Geometry/MainWidget")

        if mainWidgetGeometry!=None :
            self.restoreGeometry(mainWidgetGeometry)



    def button_browse_clicked(self,checked=False):
        lastFilePath=self.settings.value("LastFilePath")

        dialog=QFileDialog()

        # restore last file path if exist
        if lastFilePath!=None :
            if len(lastFilePath) > 0 :
                if QDir(lastFilePath).exists() :
                    dialog.setDirectory(lastFilePath)

        dialog.setNameFilter("Subtitles (*.srt)")
        file= dialog.getOpenFileName()

        if ASSERT : assert isinstance(file, tuple)

        fileName=file[0]
        self.lineEdit.setText(fileName)

        # save last file path
        fileInfo=QFileInfo(fileName)
        dir=fileInfo.absoluteDir()
        if ASSERT : assert isinstance(dir, QDir())
        selectedPath= dir.canonicalPath()
        self.settings.setValue("LastFilePath",selectedPath)

    def button_convert_clicked(self,checked=False):
        fileName=self.lineEdit.text()
        file=QFile(fileName)

        # check if a file is selected
        if len(fileName)==0:
            msgBox=QMessageBox()
            msgBox.setWindowTitle(" ")
            msgBox.setText("You should select a file first")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.exec_()
            return


        # get file extension
        fileInfo=QFileInfo(fileName)
        suffix= fileInfo.completeSuffix()

        # check extension
        if suffix!="srt":
            msgBox=QMessageBox()
            msgBox.setWindowTitle(" ")
            msgBox.setText("You should select a file with srt extension")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.exec_()
            return

        # check if file exist
        if file.exists():
            converter=Converter(fileName)
            converter.convert()

            msgBox=QMessageBox()
            msgBox.setWindowTitle(" ")
            msgBox.setText("File Converted successfully")
            msgBox.setIcon(QMessageBox.Information)
            msgBox.exec_()
        else:
            msgBox=QMessageBox()
            msgBox.setWindowTitle(" ")
            msgBox.setText("The file doesn't exist")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.exec_()

    def closeEvent(self,event):
        self.settings.setValue("Geometry/MainWidget",self.saveGeometry())

app = QApplication(sys.argv)

form=Form()
form.show()

app.exec_()