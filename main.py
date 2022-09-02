from scapy.all import *
from scapy.layers.tls.all import *

load_layer('tls')

k = PrivKey('server.key')
s = TLSSession(server_rsa_key=k)
packets = sniff(offline="best_game.pcap", session=s)
for p in packets:
    p.show()