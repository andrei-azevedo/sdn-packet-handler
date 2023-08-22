import os
from scapy.all import *
from scapy.layers.inet import IP, TCP

def main():
    while(True):
        pkt, _  = sr(IP(dst="10.0.0.2")/TCP(dport=80)/Raw(RandString(size=random.randint(72, 150))))
        write_to_pcap(pkt)
        time.sleep(0.1)

def write_to_pcap(pkt):
    wrpcap(os.path.join(os.getcwd(), "temp.pcap"), pkt, append=True)
    
if __name__ == "__main__":
    main()