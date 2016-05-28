import pycurl

file=open("j8header-2b.png","wb")
c=pycurl.Curl()
c.setopt(pycurl.URL, 'http://80.84.55.200/dl/j8header-2b.png')
c.setopt(pycurl.INTERFACE,"eno1")
c.setopt(pycurl.WRITEDATA, file)
c.perform()
c.close()