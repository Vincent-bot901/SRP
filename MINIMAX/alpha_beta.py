

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


def minimax(board, depth, alpha, beta, maximize):
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
            bestVal = max(bestVal, minimax(board, depth - 1, alpha, beta,  (not maximize)))
            board.pop()
            alpha = max(bestVal, alpha)
            if alpha >= beta:
            	return bestVal
        return bestVal
    else:
        bestVal = 9999
        for move in legals:
            board.push(move)
             #når man bruger min() så finder man de laveste tal
            bestVal = min(bestVal, minimax(board, depth - 1, alpha, beta, (not maximize)))
            board.pop()
            beta = min(beta, bestVal)
            if beta <= alpha:
                return bestVal
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
        value = minimax(board, depth - 1, -10000, 10000, (not maximize))
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


def play(board):
	while not board.is_checkmate():
		print(board)
		x = str(input("Make your next move: "))
		board.push_san(x)
		print(board)
		print(NextMove(4, board, False))
		c = str(input("Make the bots move: "))
		if board == chess.Board("rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1"):
			c = "e7e5"
			print(board)
		if board == chess.Board("rnbqkbnr/pppp1ppp/8/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2"):
			c = "b8c6"
		if board == chess.Board("r1bqkbnr/pppp1ppp/2n5/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R b KQkq - 3 3"):
			c = 'g8f6'
		if board == chess.Board("r1bqkb1r/pppp1ppp/2n2n2/4p1N1/2B1P3/8/PPPP1PPP/RNBQK2R b KQkq - 5 4"):
			c = 'f8c5'
		if board == chess.Board("r1bqk2r/pppp1Npp/2n2n2/2b1p3/2B1P3/8/PPPP1PPP/RNBQK2R b KQkq - 0 5"):
			c = 'c5f2'
		if board == chess.Board("r1bqk2r/pppp1Npp/2n2n2/4p3/2B1P3/8/PPPP1bPP/RNBQ1K1R b kq - 1 6"):
			c = 'd8e7'
		if board == chess.Board("r1b1k2N/ppppq1pp/2n2n2/4p3/2B1P3/8/PPPP1bPP/RNBQ1K1R b q - 0 7"):
			c = 'd7d5'
		if board == chess.Board("r1b1k2N/ppp1q1pp/2n2n2/3Pp3/2B5/8/PPPP1bPP/RNBQ1K1R b q - 0 8"):
			c = 'c6d4'
		if board == chess.Board("r1b1k2N/ppp1q1pp/5n2/3Pp3/2Bn4/2P5/PP1P1bPP/RNBQ1K1R b q - 0 9"):
			c = 'c1g4'	
		if board == chess.Board("r3k2N/ppp1q1pp/5n2/3Pp3/Q1Bn2b1/2P5/PP1P1bPP/RNB2K1R b q - 2 10"):
			c = 'f6d7'	
		board.push_san(c)

board = chess.Board('r3k2N/ppp1q1pp/5n2/3Pp3/2Bn2b1/2P5/PP1P1bPP/RNBQ1K1R w q - 1 10')
play(board)


