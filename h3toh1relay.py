#!/usr/bin/env python3
#h4 recieve packet and forward it to s3-eth1
from scapy.all import *

def send_to_s1(packets):
    print(f"{len(packets)} packets to s1")
    sendp(packets,iface='h3-eth0')
        
#h1-eth1 to h4-eth1 
conf.iface="h3-eth1"
#sniff broadcast 
print("running")
#sniff lldp brodcast
sniff(prn=send_to_s1)
