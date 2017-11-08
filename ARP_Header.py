#ARP Header Def

from struct import *

class ARP :

        def __init__(self, data=None):
                if data != None:
                        self._type = data[:2]
                        self._ptype = data[2:4]
                        self._len = data[4:5]
                        self._plen = data[5:6]
                        self._opcode = data[6:8]
                        self._sMAC = data[8:14]
                        self._sIP = data[14:18]
                        self._dMAC = data[18:24]
                        self._dIP = data[24:28]
                else:
                        self._type = b''
                        self._ptype = b''
                        self._len = b''
                        self._plen = b''
                        self._opcode = b''
                        self._sMAC = b''
                        self._sIP = b''
                        self._dMAC = b''
                        self._dIP = b''

        def header(self):
                return self._type + self._ptype + self._len + self._plen + self._opcode + self._sMAC + self._sIP + self._dMAC + self._dIP

        @property
        def type(self):
                (type,) = unpack('!H', self._type)
                return type

        @type.setter
        def type(self, type):
                self._type = pack('!H', type)

        @property
        def ptype(self):
                (ptype,) = unpack('!H', self._ptype)
                return ptype

        @ptype.setter
        def ptype(self, ptype):
                self._ptype = pack('!H', ptype)

        @property
        def len(self):
                (len,) = unpack('!B', self._len)
                return len

 @len.setter
        def len(self, len):
                self._len = pack('!B', len)

        @property
        def plen(self):
                (plen,) = unpack('!B', self._plen)
                return plen
        @plen.setter
        def plen(self, plen):
                self._plen = pack('!B', plen)

        @property
        def opcode(self):
                (opcode,) = unpack('!H', self._opcode)
                return opcode

        @opcode.setter
        def opcode(self, opcode):
                self._opcode = pack('!H', opcode)


        @property
        def sMAC(self):
                raw = unpack('!BBBBBB', self._sMAC)
                sMAC = "%02X:%02X:%02X:%02X:%02X:%02X" % raw
                return sMAC

        @sMAC.setter
        def sMAC(self, sMAC):
                sMAC = sMAC.split(':')
                for i in range(6) : sMAC[i] = int(sMAC[i], base=16 )
                self._sMAC = pack('!BBBBBB', sMAC[0], sMAC[1], sMAC[2], sMAC[3], sMAC[4], sMAC[5] )

        @property
        def dMAC(self):
                raw = unpack('!BBBBBB', self._dMAC)
                dMAC = "%02X:%02X:%02X:%02X:%02X:%02X" % raw
                return dMAC

        @dMAC.setter
        def dMAC(self, dMAC):
                dMAC = dMAC.split(':')
                for i in range(6) : dMAC[i] = int(dMAC[i], base=16)
                self._dMAC = pack('!BBBBBB', dMAC[0], dMAC[1], dMAC[2], dMAC[3], dMAC[4], dMAC[5] )

        @property
        def sIP(self):
                raw = unpack('!BBBB', self._sIP)
                sIP = "%d.%d.%d.%d" % raw

 @sIP.setter
        def sIP(self, sIP):
                sIP = sIP.split('.')
                for i in range(4) : sIP[i] = int(sIP[i])
                self._sIP = pack('!BBBB', sIP[0], sIP[1], sIP[2], sIP[3] )

        @property
        def dIP(self):
                raw = unpack('!BBBB', self._dIP)
                dIP = "%d.%d.%d.%d" % raw
                return dIP

        @dIP.setter
        def dIP(self, dIP):
                dIP = dIP.split('.')
                for i in range(4) : dIP[i] = int(dIP[i])
                self._dIP = pack('!BBBB', dIP[0], dIP[1], dIP[2], dIP[3] )
