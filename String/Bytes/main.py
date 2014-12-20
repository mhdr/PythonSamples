__author__ = 'Mahmood'

import codecs

msg="Hello World"

# get chars
outc=[]
for c in msg :
    outc.append(c)
print(outc)

# convert string to bytes
outputByte=str.encode(msg)
print(outputByte)

# hex
outb=[]
for c in outputByte :
    outb.append(c)
print(outb)

# convert bytes to string
outputStr=bytes.decode(outputByte)
print(outputStr)