# @Project : block_extraction
# @Filename: fragment
# @Date    : 2017-03-24
# @Author  : Shiyue Nie


class Fragment:

    # tag: str
    # description: str
    # coordinate: list with 4 cornered points, each in form of (x, y)

    def __init__(self, tag='', transcription='', coordinate=[(0, 0), (0, 0), (0, 0), (0, 0)]):
        self.tag = tag
        self.transcription = transcription
        self.coordinate = coordinate

    def settag(self, tag):
        self.tag = tag
        #return print("Tag: %s" % self.tag)

    def settranscription(self, transcription):
        self.transcription = transcription
        #return print("Description: %s" % self.transcription)

    def setcoordinate(self, coordinate):
        self.coordinate = coordinate
        #return print("Coordinate: %s" % (self.coordinate,))

    def setfragment(self, ntag, ntranscription, ncoordinate):
        self.settag(ntag)
        self.settranscription(ntranscription)
        self.setcoordinate(ncoordinate)

        #return nfragment.__dict__
        return self.__dict__