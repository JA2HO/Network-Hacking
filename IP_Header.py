#IP Header Def

from struct import *

class IP :

        def __init__(self, data=None):
                if data != None:
                        self._ver = data[:1]
                        self._serv = data[1:2]
                        self._len = data[2:4]
                        self._iden = data[4:6]
                        self._frag = data[4:6]
                        self._flag = data[6:8]
                        self._offset = data[6:8]
                        self._ttl = data[8:9]
                        self._ptype = data[9:10]
                        self._chksum = data[10:12]
                        self._sIP = data[12:16]
                        self._dIP = data[16:20]
                else:
                        self._ver = b''
                        self._serv = b''
                        self._len = b''
                        self._iden = b''
                        self._flag = b''
                        self._offset= b''
                        self._ttl = b''
                        self._ptype = b''
                        self._chksum = b''
                        self._sIP = b''
                        self._dIP = b''

        @property
        def header(self):
                (flag,) = unpack('!H', self._flag )
                (offset,) = unpack('!H', self._offset)

                flag_offset = flag + offset
                flag_offset = pack('!H', flag_offset)
                if(self._sIP =='192.168.4.30' or self._dIP=='192.168.4.30'):
                        return self._ver+self._serv+self._len+self._iden+self._frag +self._ttl+self._pty
pe+self._chksum+self._sIP+self._dIP
                else:
                        return self._ver+self._serv+self._len+self._iden+ flag_offset + self._ttl+self._
ptype+self._chksum+self._sIP+self._dIP

        @property
        def ver(self):
                (ver,) = unpack('!B', self._ver)
                return ver
        @ver.setter
        def ver(self, ver): 
	self._ver = pack('!B', ver)

        @property
        def serv(self):
                (serv,) = unpack('!B', self._serv)
                return serv
        @serv.setter
        def serv(self, serv):
                self._serv = pack('!B', serv)
@property
        def iden(self):
                (iden,) = unpack('!H', self._iden)
                return iden
        @iden.setter
        def iden(self, iden):
                self._iden = pack('!H', iden)


        @property
        def ttl(self):
                (ttl,) = unpack('!B', self._ttl)
                return ttl
        @ttl.setter
        def ttl(self, ttl):
                self._ttl = pack('!B', ttl)


        @property
        def ptype(self):
                (ptype,) = unpack('!B',self._ptype)
                return ptype
        @ptype.setter
        def ptype(self, ptype):
                self._ptype = pack('!B', ptype)


        @property
        def chksum(self):
                (chksum,) = unpack('!H', self._chksum)
                return chksum
        @chksum.setter
        def chksum(self, chksum):
                self._chksum = pack('!H', chksum)


        @property
        def sIP(self):
                raw = unpack('!BBBB', self._sIP)
                sIP = "%d.%d.%d.%d" % raw
                return sIP
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


        @property
        def len(self):
                (len,) = unpack('!H', self._len)
                return len
        @len.setter
        def len(self, len):
                self._len = pack('!H', len)

        @property
        def frag(self):
                (frag,) = unpack('!H', self._frag)
                return frag
        @frag.setter
        def frag(self,frag):
                self._frag = pack('!H', frag)

        @property
        def flag(self):
                (flag,) = unpack('!H', self._flag)
                flag = flag & 0xE000
                flag = flag >> 13
                return flag
        @flag.setter
        def flag(self, flag):
                flag = flag << 13
                self._flag = pack('!H', flag)

        @property
        def offset(self):
                (offset,) = unpack('!H', self._offset)
                offset = offset & ox1FFF
                offset = offset << 3
                return offset
        @offset.setter
        def offset(self, offset):
                offset = offset >> 3
                self._offset = pack('!H', offset)
