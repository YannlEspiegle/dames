#!/usr/bin/env python3

from board import Board
from constants import TAILLE_CASE
from endscreen import draw_endscreen


class Game:
    def __init__(self, window):
        self.win = window

        self.trait = 1  # 1 = trait aux blancs, 2 = trait aux noirs
        self.board = Board(window)
        self.tours_sans_prises = 0
        self.partie_finie = False
        self.winner = 0

    def draw(self):
        self.board.draw()

    def tour_suivant(self):
        if self.trait == 1:
            self.trait = 2
        else:
            self.trait = 1

    def onclick(self, pos):
        if not self.partie_finie:
            # on récupère les coordonnées de la pièce sur le plateau
            case = (pos[0] // TAILLE_CASE, pos[1] // TAILLE_CASE)

            if not self.board.piece_est_touchee:
                if self.board.get_color(case) == self.trait:
                    self.board.select(case)
            else:
                # si une piece est déja selectionnée, on la déplace
                est_legal = self.board.deplacer(self.board.piece_touchee, case)
                self.board.deselect()
                if est_legal:
                    self.tour_suivant()
