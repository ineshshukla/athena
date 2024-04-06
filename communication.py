import sys
import chess
import argparse
from moves import aiMove


# python lichess-bot.py -u
# venv\Scripts\activate  
def talk():
    """
    The main input/output loop.
    This implements a slice of the UCI protocol.
    """
    board = chess.Board()

    while True:
        msg = input()
        command(board, msg)


def command(board: chess.Board, msg: str):
    """
    Accept UCI commands and respond.
    The board state is also updated.
    """
    msg = msg.strip()
    tokens = msg.split(" ")
    while "" in tokens:
        tokens.remove("")

    if msg == "quit":
        sys.exit()

    if msg == "uci":
        print("id name Athena-AI")  # Andrew/Roma -> And/oma
        print("id author Inesh Shukla")
        print("uciok")
        return

    if msg == "isready":
        print("readyok")
        return

    if msg == "ucinewgame":
        return

    if msg.startswith("position"):
        if len(tokens) < 2:
            return

        # Set starting position
        if tokens[1] == "startpos":
            board.reset()
            moves_start = 2
        elif tokens[1] == "fen":
            fen = " ".join(tokens[2:8])
            board.set_fen(fen)
            moves_start = 8
        else:
            return

        # Apply moves
        if len(tokens) <= moves_start or tokens[moves_start] != "moves":
            return

        for move in tokens[(moves_start+1):]:
            board.push_uci(move)

    if msg == "d":
        # Non-standard command, but supported by Stockfish and helps debugging
        print(board)
        print(board.fen())

    if msg[0:2] == "go":
        _move = aiMove( board)
        print(f"bestmove {_move}")
        return
