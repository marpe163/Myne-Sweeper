from TileBoard import TileBoard

def CheckBoardForWin(board):
    for x in range(board.width):
        for y in range(board.height):
            currentTile = board.getTile(x,y)
            if currentTile.isBomb:
                if not currentTile.isFlagged:
                    return False
                else:
                    continue
            else:
                if currentTile.isFlagged:
                    return False
                    
                elif not currentTile.isClicked:
                    return False
    return True
