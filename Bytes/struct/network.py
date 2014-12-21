__author__ = 'mahmood'

import struct

# for using in network

data="Mahmood"
dataB=str.encode(data)
length=len(dataB)
print("Length : ",length)

length4=struct.pack("i",length)
dataToSend=length4+dataB
print(dataToSend)


lengthUnpacked=struct.unpack("i",dataToSend[0:4])
print(lengthUnpacked[0])
print(dataToSend[4:4+lengthUnpacked[0]])