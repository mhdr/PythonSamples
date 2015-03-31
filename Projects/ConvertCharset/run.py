#!/usr/bin/python

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from Converter import Converter


class Form(QWidget):
    def __init__(self,parent=None):
        super(Form, self).__init__(parent)

        self.setFixedHeight(150)
        self.setWindowTitle("Subtitle Converter")

        self.label=QLabel("File")

        self.lineedit=QLineEdit()
        self.lineedit.setFixedWidth(600)
        self.lineedit.setReadOnly(True)

        self.button_browse=QPushButton("Browse...")
        self.button_browse.clicked.connect(self.button_browse_clicked)

        self.button_convert=QPushButton("Convert")
        self.button_convert.clicked.connect(self.button_convert_clicked)

        self.layout=QHBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.lineedit)
        self.layout.addWidget(self.button_browse)
        self.layout.addWidget(self.button_convert)

        self.setLayout(self.layout)

    def button_browse_clicked(self,checked=False):
        dialog=QFileDialog()
        dialog.setNameFilter("Subtitles (*.srt)")
        file= dialog.getOpenFileName()
        fileName=file[0]
        self.lineedit.setText(fileName)


    def button_convert_clicked(self,checked=False):
        fileName=self.lineedit.text()
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

app = QApplication(sys.argv)

form=Form()
form.show()

app.exec_()