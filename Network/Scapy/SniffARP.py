from scapy.all import *

print sniff(filter="arp",count=10).summary()