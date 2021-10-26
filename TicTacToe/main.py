import pygame
from constants import *
from board import Board
from pieces import *

pygame.init()

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

clock = pygame.time.Clock()

board = Board(screen)

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.make_move()

            winner = board.check_game()

            if winner and winner != -1:
                print("Circle wins!" if type(winner) == Circle else "Cross wins!")
            if winner == -1:
                print("DRAW!")
                

    screen.fill((0, 0, 0))

    board.draw_board()
    board.draw_pieces()
    pygame.display.flip()
