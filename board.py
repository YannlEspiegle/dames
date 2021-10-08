#!/usr/bin/env python3


import pygame as pg

from constants import BLACK, PIECES, TAILLE_CASE, WHITE


class Board:
    def __init__(self, win):
        self.win = win  # besoin pour la fonction draw
        self.tour_joueur = 1
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
                    piece = pg.image.load(PIECES[self.plateau[y][x]])
                    piece = pg.transform.scale(piece, (taille, taille))
                    self.win.blit(piece, (x * taille, y * taille))
