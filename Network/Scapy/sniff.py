from scapy.all import *

packets=sniff(count=10)

print(packets[0].summary())