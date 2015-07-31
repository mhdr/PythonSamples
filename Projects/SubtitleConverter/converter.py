import codecs
import shutil
import os

class Converter :
    def __init__(self,fileName):
        """
        @:type fileName: string
        :param fileName:
        :return:
        """
        self.fileName=fileName

    def create_backup(self):
        # create backup
        backupFileName="{0}.bak".format(self.fileName)
        shutil.copy2(self.fileName,backupFileName)

    def convert(self):
        self.create_backup()

        # read content of file
        sourceFile= codecs.open(self.fileName,"r","Windows-1256")
        contents=sourceFile.read()
        sourceFile.close()
        # remove file to create a new one with utf-8 charset
        os.remove(self.fileName)

        # write contents to file with utf-8 charset
        target_file=codecs.open(self.fileName,"w","utf-8-sig")
        target_file.write(contents)
        target_file.close()
