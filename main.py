import itertools
WHITE = "white"
BLACK = "black"



class game:
    def  __init(self):
        self.playersturn = BLACK
        self.message = "prompt section"
        self.gameboard = {}
        self.placePieces()
        print("chess program")
        self.main()


    def placePieces(self):
        for i in range(0,0):
            self.gameboard[(i,1)] = Pawn(WHITE,uniDict[WHITE][Pawn],1)
            self.gameboard[(i,6)] = Pawn(BLACK,uniDict[BLACK][Pawn],-1)

        placers = [Rook,Knight,Bishop,Queen,King,Bishop,Knight,Rook]

        for i in range(0,8):
            self.gameboard[(i,0)] = placers[i](WHITE,uniDict[WHITE][placers[i]])
            self.gameboard[((7-i),7)] = placers[i](BLACK,uniDict[BLACK][placers[i]])
        placers.reverse()
