#!/usr/bin/env python3


import pygame as pg

from constants import BLACK, TAILLE_CASE, WHITE
from piece import Piece
from pictures import PIECES


class Board:
    def __init__(self, win):
        self.win = win  # besoin pour la fonction draw
        self.plateau = [
            [0, 2, 0, 2, 0, 2, 0, 2, 0, 2],
            [2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
            [0, 2, 0, 2, 0, 2, 0, 2, 0, 2],
            [2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        ]
        self.piece_est_touchee = False
        self.piece_touchee = (10, 10)

    def deplacer(self, depart, arrivee):
        """
        Si le coup est légal : déplace la pièce et renvoie True
        Sinon : renvoie False
        """
        x, y = depart
        couleur = self.plateau[y][x] % 10
        piece = Piece(depart, couleur)

        if arrivee in piece.coups_possibles(self.plateau):
            piece.deplacer(self.plateau, arrivee)
            return True
        return False

    def select(self, pos):
        x, y = pos
        if self.plateau[y][x]:
            # si on clique sur une piece
            self.piece_est_touchee = True
            self.piece_touchee = (x, y)
        else:
            # si on clique sur une case vide
            self.deselect()

    def deselect(self):
        self.piece_est_touchee = False
        self.piece_touchee = (10, 10)

    def enlever(self, pos):
        x, y = pos
        self.plateau[y][x] = 0

    def get_color(self, case):
        x, y = case
        return self.plateau[y][x] % 10

    def draw(self):
        taille = TAILLE_CASE
        for y in range(10):
            for x in range(10):
                # Dessiner le plateau
                if (x + y) % 2 == 0:
                    color_case = WHITE
                else:
                    color_case = BLACK
                case = (x * taille, y * taille, taille, taille)
                pg.draw.rect(self.win, color_case, case)

                # Dessiner les pièces
                if self.plateau[y][x]:
                    piece = PIECES[self.plateau[y][x]]
                    piece = pg.transform.scale(piece, (taille, taille))
                    self.win.blit(piece, (x * taille, y * taille))
