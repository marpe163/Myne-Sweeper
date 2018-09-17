import sys
from Tile import Tile
from random import randint

class TileBoard:
    def __init__(self, width, height):
        self.board = [[Tile() for j in range(height)] for i in range(width)]
        self.width = width
        self.height = height
        self.isInitialized = False

    def getTile(self, xIdx, yIdx):
        if (not xIdx < self.width) and (not yIdx < self.height):
            print "Index Out of Range"
        else:
            return self.board[xIdx][yIdx]

    def incrementBombCountForAdjacentTiles(self, xIdx, yIdx):
        for x in range(max([0, (xIdx - 1)]), min([(xIdx + 2), self.width])):
            for y in range(max([0, (yIdx - 1)]), min([(yIdx + 2), self.height])):
                #We consider a bomb to be adjacent to itself
                self.getTile(x,y).incementNumberOfAdjacentBombsByOne()

    def initializeBoard(self, numberOfBombs):
        if numberOfBombs > (self.height * self.width):
            print "Too many bombs"
        elif numberOfBombs == 0:
            print "No Bombs!?"
        else:
            for i in range(numberOfBombs):
                while True:
                    randXIdx = randint(0, self.width - 1)
                    randYIdx = randint(0, self.height - 1)
                    currentTile = self.getTile(randXIdx, randYIdx)
                    currentTileIsBomb = self.getTile(randXIdx, randYIdx).isBomb
                    
                    if not currentTileIsBomb:
                        currentTile.setIsBomb(True)
                        self.incrementBombCountForAdjacentTiles(randXIdx, randYIdx)
                        break

    #For Debugging Purposes
    def printBoard(self):
        for it in range(self.height):
            for jt in range(self.width):
                currentTileIsBomb = self.getTile(jt, it).isBomb
                printChar = 'B' if currentTileIsBomb else 'X' 
                sys.stdout.write(printChar)
            sys.stdout.write('\n')
        sys.stdout.write('\n')
        for it in range(self.height):
            for jt in range(self.width):
                printChar = (str)(self.getTile(jt,it).numberOfAdjacentBombs)
                sys.stdout.write(printChar)
            sys.stdout.write('\n')
    def printEachTile(self,fcn):
        for it in range(self.height):
            for jt in range(self.width):
                bool1 = "True" if fcn(self.getTile(jt, it)) else "False"
                sys.stdout.write(bool1)
            sys.stdout.write('\n')
        sys.stdout.write('\n')
