#ICMP Header Def

from struct import *

class ICMP :

        def __init__(self, data=None):
                if data != None:
                        self._type = data[:1]
                        self._code = data[1:2]
                        self._chksum = data[2:4]
                        self._icmpdata = data[4:]
        @property
        def header(self):
                return self._type + self._code + self._chksum + self._icmpdata

        @property
        def type(self):
                (type,) = unpack('!B', self._type)
                return type
        @type.setter
        def type(self, type):
                self._type = pack('!B', type)

        @property
        def code(self):
                (code,) = unpack('!B', self._code)
                return code
        @code.setter
        def code(self, code):
                self._code = pack('!B', code)

        @property
        def chksum(self):
                (chksum,) = unpack('!H', self._chksum)
                return chksum
        @chksum.setter
        def chksum(self, chksum):
                self._chksum = pack('!H', chksum)

        @property
        def icmpdata(self):
                return self._icmpdata.decode(errors='ignore')
        @icmpdata.setter
        def icmpdata(self, icmpdata):
                self._icmpdata = str(icmpdata).encode('utf-8')
