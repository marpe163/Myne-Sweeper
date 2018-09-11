class Tile:
    def __init__(self, isBomb):
        self.isBomb = isBomb
        self.isClicked = False
        self.isFlagged = False
        self.numberOfAdjacentBombs = 0

    def clickTile(self):
        if not self.isFlagged:
            self.isClicked = True
        else:
            #nop

    def toggleFlag(self):
        self.isFlagged = True if not self.isFlagged else False

    def setNumberOfAdjacentBombs(self, numberOfAdjacentBombs):
        self.numberOfAdjacentBombs = numberOfAdjacentBombs

    def toggleBomb(self):
        self.isBomb = True if not self.isBomb else False

