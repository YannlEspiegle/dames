#!/usr/bin/env python3

from board import Board
from endscreen import draw_endscreen

from random import choice

class Game:
    def __init__(self, window):
        self.win = window
        self.trait = 1  # 1 = trait aux blancs, 2 = trait aux noirs
        self.board = Board(window)
        self.tours_sans_prises = 0
        self.partie_finie = False
        self.winner = 0

    def draw(self):
        if not self.partie_finie:
            self.board.draw()
        else:
            draw_endscreen(self.win, self.winner)

    def onclick(self, pos):
        if not self.partie_finie:
            self.partie_finie = True
            self.winner = choice([1, 2])
