import pygame
from constants import *
from pieces import *

class Board:

    def __init__(self,screen):
        self.screen = screen
        self.board = [[None for i in range(3)] for j in range(3)]
        self.squares = []
        self.turn = Circle
        self.squaresize = (DISPLAY_WIDTH - LINEWIDTH * 4) // 3
        for i in range(3):
            for j in range(3):
                self.squares.append(Square((i, j),pygame.Rect(i * self.squaresize +  (i + 1) * LINEWIDTH, j * self.squaresize + (j + 1) * LINEWIDTH, self.squaresize, self.squaresize)))

    def draw_board(self):
        for square in self.squares:
            pygame.draw.rect(self.screen, (255, 255, 255), square)

    def draw_pieces(self):
        for row in self.board:
            for piece in row:
                if type(piece) == Circle:
                    pos = piece.rect.rect
                    pygame.draw.circle(self.screen, (0, 0, 0), (pos[0] + self.squaresize // 2, pos[1] + self.squaresize // 2), int(self.squaresize * 0.4))
                    pygame.draw.circle(self.screen, (255, 255, 255), (pos[0] + self.squaresize // 2, pos[1] + self.squaresize // 2), int(self.squaresize * 0.36))

                if type(piece) == Cross:
                    pos = piece.rect.rect
                    pygame.draw.line(self.screen, (0, 0, 0), (pos[0] + int(self.squaresize * 0.1), pos[1] + int(self.squaresize * 0.1)), (pos[0] + int(self.squaresize * 0.9), pos[1] + int(self.squaresize * 0.9)), int(self.squaresize * 0.06))
                    pygame.draw.line(self.screen, (0, 0, 0), (pos[0] + int(self.squaresize * 0.9), pos[1] + int(self.squaresize * 0.1)), (pos[0] + int(self.squaresize * 0.1), pos[1] + int(self.squaresize * 0.9)), int(self.squaresize * 0.06))



    def check_game(self):
        board = self.board
        for row in board:

            if row[0] and type(row[0]) == type(row[1]) and type(row[1]) == type(row[2]):

                return row[0]

        flipped = list(zip(*board))
        for row in flipped:
            if all(row) and type(row[0]) == type(row[1]) and type(row[1]) == type(row[2]):
                return row[0]

        if board[0][0] and type(board[0][0]) == type(board[1][1]) and type(board[1][1]) == type(board[2][2]):
            return board[0][0]

        if board[0][2] and type(board[0][2]) == type(board[1][1]) and type(board[1][1]) == type(board[2][0]):
            return board[0][2]

        for row in board:
            if not all(row):
                return None

        return "Draw"


    def make_move(self):
        square_selected = None
        for square in self.squares:
            if square.rect.collidepoint(pygame.mouse.get_pos()):
                square_selected = square
                break
        if square_selected and not self.board[square_selected.pos[1]][square_selected.pos[0]]:

            pos = square_selected.pos
            self.board[pos[1]][pos[0]] = Circle(pos, square_selected) if self.turn == Circle else Cross(pos, square_selected)
            self.turn = Circle if self.turn == Cross else Cross
