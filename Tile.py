class Tile:
    def __init__(self):
        self.isBomb = False
        self.isClicked = False
        self.isFlagged = False
        self.numberOfAdjacentBombs = 0

    def clickTile(self):
        if not self.isFlagged:
            self.isClicked = True
        #else: NOOP 

    def toggleFlag(self):
        self.isFlagged = True if not self.isFlagged else False

    def setNumberOfAdjacentBombs(self, numberOfAdjacentBombs):
        self.numberOfAdjacentBombs = numberOfAdjacentBombs
    def incementNumberOfAdjacentBombsByOne(self):
        self.numberOfAdjacentBombs = self.numberOfAdjacentBombs + 1

    def setIsBomb(self, isBomb):
        self.isBomb = isBomb 


