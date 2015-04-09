from scapy.all import *
from scapy.layers.inet import IP

a=IP(ttl=10)

print(a.src)
print(a.dst)
print(a.ttl)