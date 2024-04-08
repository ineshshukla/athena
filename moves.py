import chess
from evaluation import *
from typing import List

MATE_SCORE     = 1000000000
MATE_THRESHOLD =  999000000


def aiMove(board):
    depth=3
    transposition_table = {}
    move = negamax_root(depth, board,transposition_table)
    return move

def order(board: chess.Board)->List[chess.Move]:
    end_game=check_end_game(board)
    def orderer(move):
        return move_value(board, move,end_game)

    in_order = sorted(
        board.legal_moves, key=orderer
    )
    return list(in_order)


def quiescence_search( alpha:float,beta:float,board: chess.Board,color:int):
    stand_pat = eval(board,color)

    if stand_pat >= beta:
        return beta
    if alpha < stand_pat:
        alpha = stand_pat

    legal_captures = [move for move in board.legal_moves if board.is_capture(move)]

    for move in legal_captures:
        board.push(move)
        score = -quiescence_search(-beta, -alpha, board,-color)
        board.pop()

        if score >= beta:
            return beta

        if score > alpha:
            alpha = score

    return alpha


# def minimax(depth: int, alpha:float, beta:float, board: chess.Board, maximising: bool, transposition_table: dict) -> float:
#     position_key = board.fen()
#     if position_key in transposition_table:
#         return transposition_table[position_key]

#     if board.is_checkmate():
#         # The previous move resulted in checkmate
#         score = -MATE_SCORE if maximising else MATE_SCORE
#         transposition_table[position_key] = score
#         return score
    
#     elif board.is_game_over():
#         score = 0
#         transposition_table[position_key] = score
#         return score
    
#     if depth == 0:
#         score = quiescence_search(alpha, beta, board)
#         transposition_table[position_key] = score
#         return score
    
#     moves = order(board)
#     if maximising:
#         val = float("-inf")
#         for move in moves:
#             board.push(move)
#             val = max(val, minimax(depth-1, alpha, beta, board, not maximising, transposition_table))
#             board.pop()
#             alpha = max(alpha, val)
#             if beta <= alpha:
#                 break  # Beta cut-off
#     else:
#         val = float("inf")
#         for move in moves:
#             board.push(move)
#             val = min(val, minimax(depth-1, alpha, beta, board, not maximising, transposition_table))
#             board.pop()
#             beta = min(beta, val)
#             if beta <= alpha:
#                 break  # Alpha cut-off

#     transposition_table[position_key] = val
#     return val


def negamax(depth: int, alpha:float, beta:float, board: chess.Board, transposition_table: dict,color:int) -> float:
    if board.is_checkmate():
        # The previous move resulted in checkmate
        score = -MATE_SCORE 
        return score
    
    elif board.is_game_over():
        score = 0
        return score

    if depth==0:
        score = quiescence_search(alpha, beta, board,color)
        return score
    
    maxi = -float("inf")

    moves = order(board)
    for move in moves:
        board.push(move)
        score = -negamax(depth-1,-beta,-alpha,board,transposition_table,-color)
        board.pop()
        maxi = max(maxi, score)
        alpha = max(alpha, score)
        if alpha >= beta:
            break
    return maxi

def negamax_root(depth: int, board: chess.Board,transposition_table) -> chess.Move:
    moves=order(board)
    if board.turn == chess.WHITE:
        color=1
    else:
        color=-1
    best_move= moves[0]
    alpha = -MATE_SCORE
    beta = MATE_SCORE
    maxi = float("-inf")
    for move in moves:
        board.push(move)
        val = -negamax(depth-1, -beta, -alpha,board,transposition_table, -color)
        board.pop()
        if val > maxi:
            maxi = val
            best_move = move
        alpha = max(alpha, val)
    return best_move