

#For at finde det bedste træk skal vi først kunne evaluver en position

#Dette kan vi gøre ved at lave en matrix som fortæller os nogle af de bedste positioner for brikkerne.

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
	return WhitePoints - BlackPoints

#Nu har vi en funktion som kan evaluver en skak position. For at teste funktionen kan vi load et spil 

#For at load et spil kan vi bruge chess, png er en fil typpe som er måden et skak spil bliver gemt. 

"""  
board = chess.Board("rnbqkbnr/1p1p1pp1/2p4p/p3p1N1/2B1P3/8/PPPP1PPP/RNBQK2R w KQkq - 0 5")
print(board)
print(Evaluation(board))
"""
#https://lichess.org/analysis/standard/rnbqkbnr/1p1p1pp1/2p4p/p3p1N1/2B1P3/8/PPPP1PPP/RNBQK2R_w_KQkq_-_0_5#8

#Ved at kigge på linken kan de fleste skak spiller se at hvid klart har en fordel

#Men denne evaluver funktion kan self ikke se taktikker dette kan vi se i dette eksempel: 
"""
board = chess.Board ("r1bqkb1r/pppp1ppp/2n2n2/4p2Q/2B1P3/8/PPPP1PPP/RNB1K1NR w KQkq - 4 4")
print(board)
print(Evaluation(board))
"""
#først tjekker vi om spillet er slut, derefter tjekker vi hvem der bliv sat i skakmat 

#Derefter tjekker vi om spillet er uafgjort, hvis spillet er det så retuner vi evaluationen af skak bræted

# vi definer nu alle mulige træk som legals

# Derefter laver vi en if statement for hvis maximize er true, mazimize er true så definer vi bestval som -9999 hvilket vil sige at vi -->
#finder et træk for sort og når bestval er lig med 99999 så finder vi et træk for hvid.

#Når vi kalder på minimax så skal vi også angive hvis maximize er true eller false, dermed vælger om vi finder et træk for sort eller hvid, 

def minimax(board, depth, maximize):
    if(board.is_checkmate()):
        if(board.turn == chess.WHITE):
            return -100000
        else:
            return 1000000
    if(board.is_stalemate()) or board.is_insufficient_material():
        return 0
    if depth == 0:
        return Evaluation(board)
    legals = board.legal_moves
    #if(maximize) er de sammen som if(maximize == true) 
    if(maximize):
        bestVal = -9999
        for move in legals:
            board.push(move)
            #når man bruger max() så finder man de højeste tal
            bestVal = max(bestVal, minimax(board, depth - 1, (not maximize)))
            board.pop()
        return bestVal
    else:
        bestVal = 9999
        for move in legals:
            board.push(move)
             #når man bruger min() så finder man de laveste tal
            bestVal = min(bestVal, minimax(board, depth - 1, (not maximize)))
            board.pop()
        return bestVal

def NextMove(depth, board, maximize):
	#Vi definer igen alle mulige træk og derefter definer vi bestMove some none.
    legals = board.legal_moves
    bestMove = None
    bestValue = -9999
    #Nu laver vi en if statment for når maximize er falsk 
    if(not maximize):
        bestValue = 9999
    #Nu laver vi en loop hvor vi kigger på alle mulige træk og ser hvilken er bedst
    for move in legals:
        board.push(move)
        value = minimax(board, depth - 1, (not maximize))
        board.pop()
        if maximize:
            if value > bestValue:
                bestValue = value
                bestMove = move
        else:
            if value < bestValue:
                bestValue = value
                bestMove = move
    return (bestMove, bestValue)


board = chess.Board ("6K1/3r3r/5kn1/5p2/5P2/6N1/8/4R1R1 w - - 0 1")
print(board)
print(NextMove(5,board, True))
