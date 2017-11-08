#TCP Header Def

from struct import *
 
class TCP:
 
        def __init__(self, data=None):
                if data !=None:
                        self._sport[:2]
                        self._dport[2:4]
                        self._seqnum[4:8]
                        self._acknum[8:12]
                        self._len[12:13]
                        self._flag[13:14]
                        self._window[14:16]
                        self._chksum[16:18]
                        self._urgptr[18:20]
 
                else:
                        self._sport=b''
                        self._dport=b''
                        self._seqnum=b''
                        self._acknum=b''
                        self._len=b''
                        self._flag=b''
                        self._window=b''
                        self._chksum=b''
                        self._urgptr=b''
 
 
        @property
        def header(self):
                return self._sport+self._dport+self._seqnum+self._acknum+self._len+self._flag+self._window+self._chksum+self._urgptr
 
 
        @property
        def sport(self):
                (sport,)  = unpack('!H', self._sport)
                return sport
        @sport.setter
        def sport(self, sport):
                self._sport = pack('!H', sport)
 
 
        @property
        def dport(self):
                (dport,)  = unpack('!H', self._dport)
                return dport
        @dport.setter
        def dport(self, dport):
                self._dport = pack('!H', dport)
 
 
       @property
        def seqnum(self):
                (seqnum,)  = unpack('!L', self._seqnum)
                return seqnum
        @seqnum.setter
        def seqnum(self, seqnum):
                self._seqnum = pack('!L', seqnum)
 
 
        @property
        def acknum(self):
                (acknum,) = unpack('!L', self._acknum)
                return acknum
        @acknum.setter
        def acknum(self, acknum):
                self._acknum = pack('!L', acknum)
 
 
        @property
        def len(self):
                (len,) = unpack('!B',self._len)
                len = len>>2
                return len
        @len.setter
        def len(self,len):
                self._len = pack('!B',len << 2)
 
 
        @property
        def flag(self):
                (flag,) = unpack('!B',self._flag)
                return flag
        @flag.setter
        def flag(self,flag):
                self._flag = pack('!B',flag)
 
 
        @property
        def window(self):
                (window,) = unpack('!H',self._window)
                return window
        @window.setter
        def window(self,window):
                self._window =pack('!H',window)
 
 
        @property
        def chksum( self ):
                (chknum,) = unpack('!H', self._chksum )
                return chksum
        @chksum.setter
        def chksum( self, chksum):
                self._chksum = pack('!H', chksum)
 
 
        @property
        def urgptr( self ):
                (urgptr,) = unpack('!H',self._urgptr)
                return urgptr
        @urgptr.setter
        def urgptr( self, urgptr):
                self._urgptr = pack('!H',urgptr)
