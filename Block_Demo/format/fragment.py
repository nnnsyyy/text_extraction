# @Project : block_extraction
# @Filename: fragment
# @Date    : 2017-03-24
# @Author  : Shiyue Nie


class Fragment:

    # tag: str
    # description: str
    # coordinate: list with 4 cornered points, each in form of (x, y)
    # block: int (1-8)

    def __init__(self, tag='', transcription='', coordinate=[(0, 0), (0, 0), (0, 0), (0, 0)], block=1):
        self.tag = tag
        self.transcription = transcription
        self.coordinate = coordinate
        self.block = block

    def settag(self, tag):
        self.tag = tag
        #return print("Tag: %s" % self.tag)

    def settranscription(self, transcription):
        self.transcription = transcription
        #return print("Description: %s" % self.transcription)

    def setcoordinate(self, coordinate):
        self.coordinate = coordinate
        #return print("Coordinate: %s" % self.coordinate)

    def setblock(self, block):
        self.block = block
        print("Block: %s" % self.block)

    def setfragment(self, ntag, ntranscription, ncoordinate):
        self.settag(ntag)
        self.settranscription(ntranscription)
        self.setcoordinate(ncoordinate)
        #self.setblock(nblock)

        #return nfragment.__dict__
        return self.__dict__