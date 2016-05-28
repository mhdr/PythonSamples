import pycurl

file=open("01.jpg","wb")
c=pycurl.Curl()
c.setopt(pycurl.URL, 'http://80.84.55.200/dl/Swiftpack%20Swiftcheck/Swiftpack%20Swiftcheck%20(HQ).jpg')
c.setopt(pycurl.WRITEDATA, file)
c.setopt(pycurl.FOLLOWLOCATION, True)
c.setopt(pycurl.MAXREDIRS,5)
c.perform()
c.close()