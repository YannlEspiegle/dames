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
        self.piece_rafle = None

    def draw(self):
        if not self.partie_finie:
            self.board.draw()
        else:
            draw_endscreen(self.win, self.winner)

    def tour_suivant(self):
        if self.trait == 1:
            self.trait = 2
        else:
            self.trait = 1

    def abandon(self):
        if self.trait == 1:
            self.winner = 2
        else:
            self.winner = 1
        self.partie_finie = True

    def nulle(self):
        self.winner = 0
        self.partie_finie = True

    def check_fin_partie(self):
        pieces_blanches, pieces_noires = self.board.liste_pieces()

        if pieces_blanches == [10] and pieces_noires == [10]:
            self.partie_finie = True
            self.winner = 0

        if self.tours_sans_prises >= 25:
            self.partie_finie = True
            self.winner = 0

        if pieces_noires == []:
            self.partie_finie = True
            self.winner = 1

        if pieces_blanches == []:
            self.partie_finie = True
            self.winner = 2

    def onclick(self, pos):
        if not self.partie_finie:
            # on récupère les coordonnées de la case sur le plateau
            case = (pos[0] // TAILLE_CASE, pos[1] // TAILLE_CASE)

            if not self.board.piece_est_touchee:
                if self.board.get_color(case) == self.trait:
                    # Si une pièce est en train de rafler, on ne peut que jouer cette pièce là
                    if self.piece_rafle:
                        pieces_obligatoires = [self.piece_rafle]
                    else:
                        pieces_obligatoires = self.board.pieces_pouvant_prendre(self.trait)

                    if pieces_obligatoires == [] or case in pieces_obligatoires:
                        self.board.select(case)
            else:
                # si une piece est déja sélectionnée, on la déplace
                est_legal, prise = self.board.deplacer(case)

                if not prise:
                    self.tours_sans_prises += 1
                else:
                    self.tours_sans_prises = 0

                # si la pièce peut rafler (càd prendre une autre pièce après une prise)
                if prise and case in self.board.pieces_pouvant_prendre(self.trait):
                    self.piece_rafle = case
                else:
                    self.piece_rafle = None

                    self.board.deselect()
                    if est_legal:
                        self.check_fin_partie()
                        self.tour_suivant()
