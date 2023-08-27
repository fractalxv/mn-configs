#!/usr/bin/env python3
#h1 recieve lldp packet and forward it to h1-eth1(h4)
from scapy.all import *
def send_to_h4_s1(packets):
    print(f"{len(packets)} packets to h4_s1")
    sendp(packets,iface='h1-eth1')
    #sendp(packets,iface='h1-eth2')
#h1-eth0 to switch 
conf.iface="h1-eth0"
#sniff broadcast 
print("Running")
sniff(prn=send_to_h4_s1)
