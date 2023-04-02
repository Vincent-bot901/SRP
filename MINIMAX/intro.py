

#INTRO


"""
#Vi starter med at load de libraries som vi har tænkt os at bruge. 
import chess
import random
import time



#Til at starte med vil vi gerne kunne få skak bretet til at funger, dette kan vi gøre via chess library som vi allerade har loaded. 

#for at se hvordan man bruger chess library kan vi gå ind og kigge på denne link https://python-chess.readthedocs.io/en/latest/, hvilket er dens dokumentation.

#Vi starter med at lave et skak bredt hvor på vi kan spille skak:



Board = chess.Board()

#for at se bredtet kan vi printe den i terminalen


print(Board)

# for at spille skal man bruge kommandoen:


Board.push_san("e4")

print(Board)




"""

import chess

# P = 100
# N = 310
# B = 320
# R = 500
# Q = 900

# position table
pieceSquareTable = [
  [ -50,-40,-30,-30,-30,-30,-40,-50 ],
  [ -40,-20,  0,  0,  0,  0,-20,-40 ],
  [ -30,  0, 10, 15, 15, 10,  0,-30 ],
  [ -30,  5, 15, 20, 20, 15,  5,-30 ],
  [ -30,  0, 15, 20, 20, 15,  0,-30 ],
  [ -30,  5, 10, 15, 15, 10,  5,-30 ],
  [ -40,-20,  0,  5,  5,  0,-20,-40 ],
  [ -50,-40,-30,-30,-30,-30,-40,-50 ] ]


def eval(board):
    scoreWhite = 0
    scoreBlack = 0
    for i in range(0,8):
        for j in range(0,8):
            squareIJ = chess.square(i,j)
            pieceIJ = board.piece_at(squareIJ)
            if str(pieceIJ) == "P":
                scoreWhite += (100 + pieceSquareTable[i][j])
            if str(pieceIJ) == "N":
                scoreWhite += (310 + pieceSquareTable[i][j])
            if str(pieceIJ) == "B":
                scoreWhite += (320 + pieceSquareTable[i][j])
            if str(pieceIJ) == "R":
                scoreWhite += (500 + pieceSquareTable[i][j])
            if str(pieceIJ) == "Q":
                scoreWhite += (900 + pieceSquareTable[i][j])
            if str(pieceIJ) == "p":
                scoreBlack += (100 + pieceSquareTable[i][j])
            if str(pieceIJ) == "n":
                scoreBlack += (310 + pieceSquareTable[i][j])
            if str(pieceIJ) == "b":
                scoreBlack += (320 + pieceSquareTable[i][j])
            if str(pieceIJ) == "r":
                scoreBlack += (500 + pieceSquareTable[i][j])
            if str(pieceIJ) == "q":
                scoreBlack += (900 + pieceSquareTable[i][j])
    return scoreWhite - scoreBlack

board = chess.Board("rnbqkbnr/1p1p1pp1/2p4p/p3p1N1/2B1P3/8/PPPP1PPP/RNBQK2R w KQkq - 0 5")
print(board)
print(eval(board))