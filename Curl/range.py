import pycurl
import os

file_name="01.exe"
c=pycurl.Curl()
c.setopt(pycurl.URL, 'http://80.84.55.200/dl/PyQt5-5.6-gpl-Py3.5-Qt5.6.0-x32-2.exe')

if os.path.exists(file_name) :
    downloaded_size=os.path.getsize(file_name)
    c.setopt(pycurl.RESUME_FROM,downloaded_size)
    file = open(file_name, "ab")
else :
    file = open(file_name, "wb")

c.setopt(pycurl.WRITEDATA, file)
c.setopt(pycurl.RANGE,"0-10000000")

c.perform()
c.close()