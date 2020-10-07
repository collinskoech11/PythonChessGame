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


    def main(self):

        while True:
            self.printBoard()
            print(self.message)
            self.message = ""
            startpos,endpos = self.parseInput()
            try:
                target = self.gameboard[startpos]
            except:
                self.message = "could not find piece; index probably out of range"
                target = None

            if target:
                print("found "+str(target))
                if target.Color != self.playersturn:
                    self.message = "you aren't allowed to move that piece this turn"
                    continue
                if target.isValid(startpos,endpos,target.Color,self.gameboard):
                    self.message = "that is a valid move"
                    self.gameboard[endpos] = self.gameboard[startpos]
                    del self.gameboard[startpos]
                    self.isCheck()
                    if self.playersturn == BLACK:
                        self.playersturn = WHITE
                    else : self.playersturn = BLACK
                else : 
                    self.message = "invalid move" + str(target.availableMoves(startpos[0],startpos[1],self.gameboard))
                    print(target.availableMoves(startpos[0],startpos[1],self.gameboard))
            else : self.message = "there is no piece in that space"

    def isCheck(self):

        king = King
        kingDict = {}
        pieceDict = {BLACK : [], WHITE : []}
        for position,piece in self.gameboard.items():
            if type(piece) == King:
                kingDict[piece.Color] = position
            print(piece)
            pieceDict[piece.Color].append((piece,position))

            if self.canSeeKing(kingDict[WHITE],pieceDict[BLACK]):
                self.message = "white player is in check"
            if self.canSeeKing(kingDict[BLACK],pieceDict[WHITE]):
                self.message = "black player is in check"


    def canSeeKing(self,kingpos,piecelist):

        for piece,position in piecelist:
            if piece.isValid(position,kingpos,piece.Color,self.gameboard):
                return True

    def parseInput(self):
        try:
            a,b = input().split()
            a = ((ord(a[0])-97), int(a[1])-1)
            b = (ord(b[0])-97, int(b[1])-1)
            print(a,b)
            return(a,b)
        except:
            print("error decoding input. please try again")
            return((-1,-1),(-1,-1))

    """def validateInput(self, *kargs):
        for arg in kargs:
            if type(arg[0]) is not type(1) or type(arg[1]) is not type(1):
                return False
        return True"""

    def printBoard(self):
        print(" 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
        for i in range(0,8):
            print("-"*32)
            print(chr(i+97),end="|")
            for j in range(0,8):
                item = self.gameboard.get((i,j)," ")
                print(str(item)+ '|', end = " ")
            print()
        print("-"*32)


    """game class. contains the following members and methods:
    two arrays of pieces for each player
    8x8 piece array with references to these pieces
    a parse function, which turns the input from the user into a list of two tuples denoting start and end points
    a checkmateExists function which checks if either players are in checkmate
    a checkExists function which checks if either players are in check (woah, I just got that nonsequitur)
    a main loop, which takes input, runs it through the parser, asks the piece if the move is valid, and moves the piece if it is. if the move conflicts with another piece, that piece is removed. ischeck(mate) is run, and if there is a checkmate, the game prints a message as to who wins
    """