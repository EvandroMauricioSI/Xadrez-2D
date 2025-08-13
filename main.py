import pygame
from board import ChessBoard
from render import Render
from utils import load_game

def main():
    pygame.init()
    WIDTH, HEIGHT = 640, 640
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Xadrez 2D")

    clock = pygame.time.Clock()
    board = ChessBoard(load_game())
    render = Render(WIN, WIDTH, HEIGHT)
    running = True

    while running:
        clock.tick(30)
        render.draw(board.board)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                board.save_game()
                running = False
            elif event.type == pygame.KEYDOWN:
                board.handle_key_event(event)
            elif event.type == pygame.MOUSEBUTTONDOWN and not board.game_over:
                board.handle_mouse_event(event, pygame.mouse.get_pos())

if __name__ == "__main__":
    main()