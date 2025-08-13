import chess
from chess_engine import get_ai_move
from utils import is_promotion_move

class ChessBoard:
    def __init__(self, board):
        self.board = board
        self.selected_square = None
        self.player_color = True  # True = Branco, False = Preto
        self.game_over = False

    def handle_key_event(self, event):
        if event.key == pygame.K_r and (self.board.is_checkmate() or self.board.is_stalemate() or 
                                        self.board.is_insufficient_material() or 
                                        self.board.is_seventyfive_moves() or 
                                        self.board.is_fivefold_repetition()):
            self.board = chess.Board()  # Reinicia o tabuleiro
            self.game_over = False
            self.selected_square = None

    def handle_mouse_event(self, event, pos):
        x, y = pos
        SQ_SIZE = 640 // 8
        col, row = x // SQ_SIZE, y // SQ_SIZE
        square = chess.square(col, 7 - row)

        if self.selected_square is None:
            if self.board.piece_at(square) and self.board.piece_at(square).color == self.player_color:
                self.selected_square = square
        else:
            move = chess.Move(self.selected_square, square)
            if is_promotion_move(self.board, move):
                move = chess.Move(self.selected_square, square, promotion=chess.QUEEN)
            if move in self.board.legal_moves:
                self.board.push(move)
                if not self.board.is_game_over():
                    ai_move = get_ai_move(self.board)
                    if is_promotion_move(self.board, ai_move):
                        ai_move = chess.Move(ai_move.from_square, ai_move.to_square, promotion=chess.QUEEN)
                    self.board.push(ai_move)
                else:
                    self.game_over = True
            self.selected_square = None

    def save_game(self):
        with open("saves/last_game.pkl", "wb") as f:
            pickle.dump(self.board.fen(), f)