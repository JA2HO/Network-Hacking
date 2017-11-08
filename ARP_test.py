#ARP Test (Broadcast)

from socket import *
from time import *

from eth import *
from arp import *

sock = socket( AF_PACKET, SOCK_RAW )
sock.bind ( ('eth0', SOCK_RAW) )

eth = Eth()
arp = Arp()

eth.dst = '00:0C:29:CC:CC:02'
eth.src = '00:0C:29:CC:CC:01'
eth.type = 0x0806

arp.HWtype = 1
arp.PTtype = 0x0800
arp.HWlen = 6
arp.PTlen = 4
arp.OPcode = 1
arp.SMACadd = '00:0C:29:CC:CC:01'
arp.SIPadd = '192.168.4.31'
arp.TMACadd = '00:00:00:00:00:00'
arp.TIPadd = '192.168.4.202'

while True:

        sock.send( eth.header + arp.header )
        sleep(1)
