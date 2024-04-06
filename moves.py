import chess
from evaluation import *
from typing import List

def aiMove(board):
    depth=3
    move = minimax_root(depth, board)
    return move

def order(board: chess.Board)->List[chess.Move]:
    def orderer(move):
        return move_value(board, move)

    in_order = sorted(
        board.legal_moves, key=orderer, reverse=(board.turn == chess.WHITE)
    )
    return list(in_order)

def minimax(depth: int, alpha:float,beta:float,board: chess.Board,maximising)->float:
    if depth==0:
        return eval(board)
    moves=order(board)
    if maximising:
        val=float("-inf")
        for move in moves:
            board.push(move)
            val=max(val,minimax(depth-1,alpha,beta,board,not maximising))
            board.pop()
            alpha=max(alpha,val)
            if(beta <= alpha):
                return val
    else:
        val=float("inf")
        for move in moves:
            board.push(move)
            val=min(val,minimax(depth-1,alpha,beta,board,not maximising))
            board.pop()
            beta = min(beta, val)
            if(beta <= alpha):
                return val
    return val

def minimax_root(depth: int, board: chess.Board) -> chess.Move:
    moves=order(board)
    maximize = board.turn == chess.WHITE
    best_move= moves[0]
    best_move_val = -float("inf") if maximize else float("inf")
    for move in moves:
        board.push(move)
        val=minimax(depth-1,-float("inf"),float("inf"),board,not maximize)
        board.pop()
        if maximize and val >= best_move_val:
            best_move_val = val
            best_move = move
        elif not maximize and val <= best_move_val:
            best_move_val = val
            best_move = move
    print(best_move_val)
    return best_move
    