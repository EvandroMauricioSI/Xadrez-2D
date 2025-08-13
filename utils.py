import chess
import pickle

def is_promotion_move(board, move):
    piece = board.piece_at(move.from_square)
    if piece and piece.piece_type == chess.PAWN:
        if piece.color == chess.WHITE and chess.square_rank(move.to_square) == 7:
            return True
        if piece.color == chess.BLACK and chess.square_rank(move.to_square) == 0:
            return True
    return False

def load_game():
    try:
        with open("saves/last_game.pkl", "rb") as f:
            fen = pickle.load(f)
            return chess.Board(fen)
    except FileNotFoundError:
        return chess.Board()