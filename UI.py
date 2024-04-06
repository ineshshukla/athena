# inspired by the https://github.com/healeycodes/andoma user interface

import chess
import argparse
from moves import aiMove

def begin():
    board= chess.Board()
    s= input("PLAY AS WHITE[W] OR BLACK[B]?")

    if s=="W" or s=="w":
        user_side=chess.WHITE
    else:
        user_side=chess.BLACK
    
    if user_side==chess.WHITE:
        print(render(board))
        board.push(getMove(board))
       
    while not board.is_game_over():
        board.push(aiMove(board))
        print(render(board))
        board.push(getMove(board))
    
    print(board.result)
    

def render(board: chess.Board):
    boardString = list(str(board))
    pieces = {
        "R": "♖",
        "N": "♘",
        "B": "♗",
        "Q": "♕",
        "K": "♔",
        "P": "♙",
        "r": "♜",
        "n": "♞",
        "b": "♝",
        "q": "♛",
        "k": "♚",
        "p": "♟",
        ".": "·",
    }

    for idx, char in enumerate(boardString):
        if char in pieces:
            boardString[idx] = pieces[char]

    ranks = ["1", "2", "3", "4", "5", "6", "7", "8"]

    display = []
    for rank in "".join(boardString).split("\n"):
        display.append(f"  {ranks.pop()} {rank}")
    if board.turn == chess.BLACK:
        display.reverse()
    display.append("    a b c d e f g h")
    return "\n" + "\n".join(display)


def getMove(board: chess.Board)-> chess.Move:
    move = input(f"\nYour move (e.g. {list(board.legal_moves)[0]}):\n")

    for legal in  board.legal_moves:
        if move== str(legal):
            return legal
        
    return getMove(board)

if __name__ == "__main__":
    try:
        begin()
    except KeyboardInterrupt:
        pass