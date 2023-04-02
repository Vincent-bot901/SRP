import chess
p = 100
n = 300
b = 300
r = 500 
q = 900

Matrix = [ 
[-50, -40,-30,-30,-30,-30,-40,-50],
[-40,-20, 0, 0, 0, 0, -20, -40],
[-30, 0, 10, 15, 15, 10, 0, -30],
[-30, 5, 15, 20, 20, 15, 5, -30],
[-30, 0, 10, 20, 20, 10, 0, -30],
[-30, 5, 10, 15, 15, 10, 5, -30], 
[-40,-20, 0, 5, 5, 0, -20, -40],
[-50, -40,-30,-30,-30,-30,-40,-50]]

#Nu giver vi alle brikker nogle point baseret på deres forskellige værdier og derudover tjekker vi positionen og evaulver hvem har den bedste position
def Evaluation(board):
	WhitePoints = 0
	BlackPoints = 0
	#Her laver vi en x range som kigger på hvilket bogstav som brikken ligger på mens Y ser på hvilket tal brikken står på, sammen skaber de det punkt hvor brikken sidder.
	for X in range (0,8):
		for Y in range (0,8):
			Position = chess.square(X,Y)
			Brik_Position = board.piece_at(Position)
			if str(Brik_Position) == "P":
				WhitePoints += (p + Matrix[X][Y])
			if str(Brik_Position) == "N":
			 	WhitePoints += (n + Matrix[X][Y])
			if str(Brik_Position) == "B":
			 	WhitePoints += (b + Matrix[X][Y])
			if str(Brik_Position) == "R":
			 	WhitePoints += (r + Matrix[X][Y])
			if str(Brik_Position) == "Q":
			 	WhitePoints += (q + Matrix[X][Y])
			if str(Brik_Position) == "p":
			 	BlackPoints += (p + Matrix[X][Y])
			if str(Brik_Position) == "n":
			 	BlackPoints += (n + Matrix[X][Y])
			if str(Brik_Position) == "b":
				BlackPoints += (b + Matrix[X][Y])
			if str(Brik_Position) == "r":
				BlackPoints += (r + Matrix[X][Y])
			if str(Brik_Position) == "q":
				BlackPoints += (q + Matrix[X][Y])
	if WhitePoints - BlackPoints == 0:
		print("Positionen er lig")
	if  WhitePoints - BlackPoints > 0:
		print("Hvid har en bedre position")
	else:
		print("Sort har en bedre position")
	print("Evaluvering:")
	return WhitePoints - BlackPoints






board = chess.Board("r1bqkb1r/ppp3pp/2n5/3Bp3/8/5Q2/PPPP1PPP/RNB1K2R b KQ - 0 8")
print(board)
print(Evaluation(board))
