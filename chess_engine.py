import chess
import random

def get_ai_move(board):
    return random.choice(list(board.legal_moves))
