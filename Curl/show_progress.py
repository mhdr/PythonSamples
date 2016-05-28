import pycurl


def progress(download_t, download_d, upload_t, upload_d):
    print("Total to download", download_t)
    print("Total downloaded", download_d)
    print("Total to upload", upload_t)
    print("Total uploaded", upload_d)

    if download_t!=0:
        progress_value = float(download_d) / float(download_t) * 100
        print("{0:.2f}%".format(progress_value))
    else:
        print("{0:.2f}%".format(0))

    print("-----------------------")


file = open("01.jpg", "wb")
c = pycurl.Curl()
c.setopt(pycurl.URL, 'http://80.84.55.200/dl/trsw11.jpg')
c.setopt(pycurl.WRITEDATA, file)
c.setopt(pycurl.NOPROGRESS, False)
c.setopt(pycurl.XFERINFOFUNCTION, progress)
c.perform()
c.close()
