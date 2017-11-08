#Ethernet Header Def

from struct import *


class Eth:

        def __init__( self, data=None ):

                if data != None:
                        self._dst = data[:6]
                        self._src = data[6:12]
                        self._type = data[12:14]

        @property
        def header( self ):
                return self._dst + self._src + self._type


        @property
        def dst( self ):
                raw = unpack('!BBBBBB', self._dst )
                dst = "%02x:%02x:%02x:%02x:%02x:%02x" % raw
                return dst
        @dst.setter
        def dst( self, dst ):
                dst = dst.split(':')
                for i in range(6):
                        dst[i] = int( dst[i], base=16 )
                self._dst = pack('!BBBBBB', dst[0],dst[1],dst[2],dst[3],dst[4],dst[5])

        @property
        def src( self ):
                raw = unpack('!BBBBBB', self._src )
                src = "%02x:%02x:%02x:%02x:%02x:%02x" % raw
                return src
        @src.setter
        def src( self, src ):
                src = src.split(':')
                for i in range(6):
                        src[i] = int( src[i], base=16 )
                self._src = pack('!BBBBBB', src[0],src[1],src[2],src[3],src[4],src[5])


        @property
        def type( self ):
                (type,) = unpack('!H', self._type )
                return type
        @type.setter
        def type( self, type ):
                self._type = pack('!H', type )
