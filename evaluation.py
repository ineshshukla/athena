import chess
import numpy as np
#this evaluataion method uses the Simplified Evaluation Function 
#https://www.chessprogramming.org/Simplifieduation_Function

import numpy as np

piece_value = {
    chess.PAWN: 100,
    chess.ROOK: 500,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.QUEEN: 900,
    chess.KING: 20000
}

# Pawn
pawn_white = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0],
    [50, 50, 50, 50, 50, 50, 50, 50],
    [10, 10, 20, 30, 30, 20, 10, 10],
    [5, 5, 10, 25, 25, 10, 5, 5],
    [0, 0, 0, 20, 20, 0, 0, 0],
    [5, -5, -10, 0, 0, -10, -5, 5],
    [5, 10, 10, -20, -20, 10, 10, 5],
    [0, 0, 0, 0, 0, 0, 0, 0]
])

pawn_black=pawn_white[::-1]

# Knight
knight_white = np.array([
    [-50, -40, -30, -30, -30, -30, -40, -50],
    [-40, -20, 0, 0, 0, 0, -20, -40],
    [-30, 0, 10, 15, 15, 10, 0, -30],
    [-30, 5, 15, 20, 20, 15, 5, -30],
    [-30, 0, 15, 20, 20, 15, 0, -30],
    [-30, 5, 10, 15, 15, 10, 5, -30],
    [-40, -20, 0, 5, 5, 0, -20, -40],
    [-50, -40, -30, -30, -30, -30, -40, -50]
])

knight_black=knight_white[::-1]

# Bishop
bishop_white = np.array([
    [-20, -10, -10, -10, -10, -10, -10, -20],
    [-10, 0, 0, 0, 0, 0, 0, -10],
    [-10, 0, 5, 10, 10, 5, 0, -10],
    [-10, 5, 5, 10, 10, 5, 5, -10],
    [-10, 0, 10, 10, 10, 10, 0, -10],
    [-10, 10, 10, 10, 10, 10, 10, -10],
    [-10, 5, 0, 0, 0, 0, 5, -10],
    [-20, -10, -10, -10, -10, -10, -10, -20]
])

bishop_black=bishop_white[::-1]

# Rook
rook_white = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0],
    [5, 10, 10, 10, 10, 10, 10, 5],
    [-5, 0, 0, 0, 0, 0, 0, -5],
    [-5, 0, 0, 0, 0, 0, 0, -5],
    [-5, 0, 0, 0, 0, 0, 0, -5],
    [-5, 0, 0, 0, 0, 0, 0, -5],
    [-5, 0, 0, 0, 0, 0, 0, -5],
    [0, 0, 0, 5, 5, 0, 0, 0]
])

rook_black=rook_white[::-1]

# Queen
queen_white = np.array([
    [-20, -10, -10, -5, -5, -10, -10, -20],
    [-10, 0, 0, 0, 0, 0, 0, -10],
    [-10, 0, 5, 5, 5, 5, 0, -10],
    [-5, 0, 5, 5, 5, 5, 0, -5],
    [0, 0, 5, 5, 5, 5, 0, -5],
    [-10, 5, 5, 5, 5, 5, 0, -10],
    [-10, 0, 5, 0, 0, 0, 0, -10],
    [-20, -10, -10, -5, -5, -10, -10, -20]
])

queen_black=queen_white[::-1]

# King (middle game)
king_white = np.array([
    [-30, -40, -40, -50, -50, -40, -40, -30],
    [-30, -40, -40, -50, -50, -40, -40, -30],
    [-30, -40, -40, -50, -50, -40, -40, -30],
    [-30, -40, -40, -50, -50, -40, -40, -30],
    [-20, -30, -30, -40, -40, -30, -30, -20],
    [-10, -20, -20, -20, -20, -20, -20, -10],
    [20, 20, 0, 0, 0, 0, 20, 20],
    [20, 30, 10, 0, 0, 10, 30, 20]
])
king_black=king_white[::-1]

king_end_game_white = np.array([
    [-50, -40, -30, -20, -20, -30, -40, -50],
    [-30, -20, -10, 0, 0, -10, -20, -30],
    [-30, -10, 20, 30, 30, 20, -10, -30],
    [-30, -10, 30, 40, 40, 30, -10, -30],
    [-30, -10, 30, 40, 40, 30, -10, -30],
    [-30, -10, 20, 30, 30, 20, -10, -30],
    [-30, -30, 0, 0, 0, 0, -30, -30],
    [-50, -30, -30, -30, -30, -30, -30, -50]
])
king_end_game_black=king_end_game_white[::-1]

def square_to_coord(square):
  
  return {0:(7,0), 1:(7,1), 2:(7,2), 3:(7,3), 4:(7,4), 5:(7,5), 6:(7,6), 7:(7,7),
          8:(6,0), 9:(6,1), 10:(6,2), 11:(6,3), 12:(6,4), 13:(6,5), 14:(6,6), 15:(6,7),
          16:(5,0), 17:(5,1), 18:(5,2), 19:(5,3), 20:(5,4), 21:(5,5), 22:(5,6), 23:(5,7),
          24:(4,0), 25:(4,1), 26:(4,2), 27:(4,3), 28:(4,4), 29:(4,5), 30:(4,6), 31:(4,7),
          32:(3,0), 33:(3,1), 34:(3,2), 35:(3,3), 36:(3,4), 37:(3,5), 38:(3,6), 39:(3,7),
          40:(2,0), 41:(2,1), 42:(2,2), 43:(2,3), 44:(2,4), 45:(2,5), 46:(2,6), 47:(2,7),
          48:(1,0), 49:(1,1), 50:(1,2), 51:(1,3), 52:(1,4), 53:(1,5), 54:(1,6), 55:(1,7),
          56:(0,0), 57:(0,1), 58:(0,2), 59:(0,3), 60:(0,4), 61:(0,5), 62:(0,6), 63:(0,7)}[square]

def position_val(board: chess.Board, square: chess.Square, piece : chess.Piece,end_game):
    x, y = square_to_coord(square)
    if piece is None:
        return 0
    elif piece.piece_type == chess.PAWN:
        return pawn_white[x][y] if piece.color == chess.WHITE else pawn_black[x][y]
    elif piece.piece_type == chess.KNIGHT:
        return knight_white[x][y] if piece.color == chess.WHITE else knight_black[x][y]
    elif piece.piece_type == chess.BISHOP:
        return bishop_white[x][y] if piece.color == chess.WHITE else bishop_black[x][y]
    elif piece.piece_type == chess.ROOK:
        return rook_white[x][y] if piece.color == chess.WHITE else rook_black[x][y]
    elif piece.piece_type == chess.QUEEN:
        return queen_white[x][y] if piece.color == chess.WHITE else queen_black[x][y]
    elif piece.piece_type == chess.KING:
        if end_game:
            return king_end_game_white[x][y] if piece.color == chess.WHITE else king_end_game_black[x][y]
        else:
            return king_white[x][y] if piece.color == chess.WHITE else king_black[x][y]

    
def evaluate_capture(board: chess.Board, move: chess.Move) -> float:
    if board.is_en_passant(move):
        return piece_value[chess.PAWN]

    captured_piece = board.piece_at(move.to_square)
    if captured_piece is None:
        return 0

    capturing_piece = board.piece_at(move.from_square)
    if capturing_piece is None:
        print(f"A piece was expected at {move.from_square}")
        return 0

    return piece_value[captured_piece.piece_type] - piece_value[capturing_piece.piece_type]


def eval(board:chess.Board,color:int):
    evaluation=0
    end_game = check_end_game(board)
    central_squares = [chess.D4, chess.E4, chess.D5, chess.E5]
    for square in chess.SQUARES:
        x, y = square_to_coord(square)
        piece = board.piece_at(square)
        piece_above=piece_below=None
        if square-8>=0 :
            piece_above=board.piece_at(square-8)
        if square+8<64:   
            piece_below=board.piece_at(square+8)
        if piece is not None:
            if piece.color == chess.WHITE:
                c=1
                if piece_above is not None and piece.piece_type==chess.PAWN and piece_above.piece_type==chess.PAWN:  #if doubled pawn then value of pawn halfed
                    c=1/2                                       
                evaluation+=c*piece_value[piece.piece_type]
                evaluation+=position_val(board,square,piece,end_game ) 
                if square in central_squares and not end_game:
                    evaluation+=25
            else:
                c=1
                if piece_below is not None and piece.piece_type==chess.PAWN and piece_below.piece_type==chess.PAWN:  #if doubled pawn then value of pawn halfed
                    c=1/2
                evaluation-=c*piece_value[piece.piece_type]
                evaluation-=position_val(board,square,piece,end_game) 
                if square in central_squares and not end_game:
                    evaluation-=25 
    if color==1:
        return evaluation
    else :
        return -evaluation

def move_value(board: chess.Board, move: chess.Move,end_game) -> float:
    end_game=check_end_game(board)
    if move.promotion is not None:
        return float("inf") if board.turn == chess.WHITE else -float("inf")
    try:
        piece=board.piece_at(move.from_square)
        position = position_val(board,move.to_square,piece,end_game)- position_val(board,move.from_square,piece,end_game)
    except:
        print(f"A piece was expected at {move.from_square}")

    capture_value = 0.0
    if board.is_capture(move):
        capture_value = evaluate_capture(board, move)

    current_value = capture_value + position

    return current_value

def check_end_game(board: chess.Board) -> bool:
    """
    - Both sides have no queens or
    - Every side which has a queen has  no other pieces or one minorpiece maximum.
    """
    queens = 0
    minors = 0

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece and piece.piece_type == chess.QUEEN:
            queens += 1
        if piece and ( piece.piece_type == chess.BISHOP or piece.piece_type == chess.KNIGHT):
            minors += 1

    if queens == 0 or (queens == 2 and minors <= 1):
        return True

    return False