__author__ = 'mahmood'

import struct

num=40
numB= struct.pack("i",num)
print(numB)

num_unpacked= struct.unpack("i",numB)

print(num_unpacked)
print(num_unpacked[0])