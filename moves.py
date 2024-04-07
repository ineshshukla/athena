import chess
from evaluation import *
from typing import List

MATE_SCORE     = 1000000000
MATE_THRESHOLD =  999000000


def aiMove(board):
    depth=3
    transposition_table = {}
    move = minimax_root(depth, board,transposition_table)
    return move

def order(board: chess.Board)->List[chess.Move]:
    end_game=check_end_game(board)
    def orderer(move):
        return move_value(board, move,end_game)

    in_order = sorted(
        board.legal_moves, key=orderer, reverse=(board.turn == chess.WHITE)
    )
    return list(in_order)


def quiescence_search( alpha:float,beta:float,board: chess.Board):
    stand_pat = eval(board)

    if stand_pat >= beta:
        return beta
    if alpha < stand_pat:
        alpha = stand_pat

    legal_captures = [move for move in board.legal_moves if board.is_capture(move)]

    for move in legal_captures:
        board.push(move)
        score = -quiescence_search(-beta, -alpha, board)
        board.pop()

        if score >= beta:
            return beta

        if score > alpha:
            alpha = score

    return alpha


def minimax(depth: int, alpha:float, beta:float, board: chess.Board, maximising: bool, transposition_table: dict) -> float:
    position_key = board.fen()
    if position_key in transposition_table:
        return transposition_table[position_key]

    if board.is_checkmate():
        # The previous move resulted in checkmate
        score = -MATE_SCORE if maximising else MATE_SCORE
        transposition_table[position_key] = score
        return score
    
    elif board.is_game_over():
        score = 0
        transposition_table[position_key] = score
        return score
    
    if depth == 0:
        score = quiescence_search(alpha, beta, board)
        transposition_table[position_key] = score
        return score
    
    moves = order(board)
    if maximising:
        val = float("-inf")
        for move in moves:
            board.push(move)
            val = max(val, minimax(depth-1, alpha, beta, board, not maximising, transposition_table))
            board.pop()
            alpha = max(alpha, val)
            if beta <= alpha:
                break  # Beta cut-off
    else:
        val = float("inf")
        for move in moves:
            board.push(move)
            val = min(val, minimax(depth-1, alpha, beta, board, not maximising, transposition_table))
            board.pop()
            beta = min(beta, val)
            if beta <= alpha:
                break  # Alpha cut-off

    transposition_table[position_key] = val
    return val


def minimax_root(depth: int, board: chess.Board,transposition_table) -> chess.Move:
    moves=order(board)
    maximize = board.turn == chess.WHITE
    best_move= moves[0]
    best_move_val = -float("inf") if maximize else float("inf")
    for move in moves:
        board.push(move)
        val=minimax(depth-1,-float("inf"),float("inf"),board,not maximize,transposition_table)
        board.pop()
        if maximize and val >= best_move_val:
            best_move_val = val
            best_move = move
        elif not maximize and val <= best_move_val:
            best_move_val = val
            best_move = move
    return best_move
    