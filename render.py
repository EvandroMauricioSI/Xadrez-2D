import pygame
import chess

class Render:
    def __init__(self, win, width, height):
        self.win = win
        self.width = width
        self.height = height
        self.SQ_SIZE = width // 8
        self.WHITE = (240, 217, 181)
        self.BROWN = (181, 136, 99)
        self.RED = (255, 0, 0)
        self.BLACK = (0, 0, 0)
        self.POPUP_BG = (200, 200, 200, 180)
        self.FONT = pygame.font.SysFont("arial", 40)
        self.PIECES = {}
        for p in ["wp","bp","wn","bn","wb","bb","wr","br","wq","bq","wk","bk"]:
            self.PIECES[p] = pygame.transform.scale(
                pygame.image.load(f"assets/{p}.png"), (self.SQ_SIZE, self.SQ_SIZE)
            )

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                color = self.WHITE if (row + col) % 2 == 0 else self.BROWN
                pygame.draw.rect(self.win, color, (col * self.SQ_SIZE, row * self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))

    def draw_pieces(self, board):
        for row in range(8):
            for col in range(8):
                square = chess.square(col, 7 - row)
                piece = board.piece_at(square)
                if piece:
                    key = piece.color and "w" or "b"
                    key += piece.symbol().lower()
                    self.win.blit(self.PIECES[key], (col * self.SQ_SIZE, row * self.SQ_SIZE))

    def draw_game_state(self, board):
        if board.is_checkmate():
            text = "Xeque-mate! Pressione R para reiniciar"
            color = self.RED
        elif board.is_stalemate() or board.is_insufficient_material() or board.is_seventyfive_moves() or board.is_fivefold_repetition():
            text = "Empate! Pressione R para reiniciar"
            color = self.BLACK
        elif board.is_check():
            text = "Xeque!"
            color = self.BLACK
            text_surface = self.FONT.render(text, True, color)
            text_rect = text_surface.get_rect(center=(self.width // 2, self.height - 30))
            self.win.blit(text_surface, text_rect)
            return
        else:
            return

        popup_width, popup_height = 500, 200
        popup_x, popup_y = (self.width - popup_width) // 2, (self.height - popup_height) // 2
        popup_surface = pygame.Surface((popup_width, popup_height), pygame.SRCALPHA)
        popup_surface.fill(self.POPUP_BG)
        text_surface = self.FONT.render(text, True, color)
        text_rect = text_surface.get_rect(center=(popup_width // 2, popup_height // 2))
        popup_surface.blit(text_surface, text_rect)
        self.win.blit(popup_surface, (popup_x, popup_y))

    def draw(self, board):
        self.draw_board()
        self.draw_pieces(board)
        self.draw_game_state(board)