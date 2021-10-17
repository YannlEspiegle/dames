#!/usr/bin/env python3


import pygame as pg

from constants import BLACK, TAILLE_CASE, WHITE
from pictures import PIECES
from piece import Piece


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
        self.piece_touchee = None
        # piece_touchee sera un objet Piece

    def deplacer(self, arrivee):
        """
        Déplace la `piece_touchee` au point d'arrivée
        Si le coup est légal : déplace la pièce et renvoie True
        Sinon : renvoie False
        """
        if arrivee in self.piece_touchee.coups_possibles(self.plateau):

            if self.piece_touchee.prises_possibles(self.plateau) != []:
                # la pièce adverse est le milieu entre l'arrivee et le départ
                piece_adverse = (
                    (self.piece_touchee.x + arrivee[0]) // 2,
                    (self.piece_touchee.y + arrivee[1]) // 2,
                )
                self.enlever(piece_adverse)

            self.piece_touchee.deplacer(self.plateau, arrivee)

            # promotions en dames
            if self.piece_touchee.couleur == 1 and arrivee[1] == 0:
                self.piece_touchee.promotion(self.plateau)
            elif self.piece_touchee.couleur == 2 and arrivee[1] == 9:
                self.piece_touchee.promotion(self.plateau)

            return True
        return False

    def pieces_pouvant_prendre(self, couleur):
        """vérifie si une couleur peut faire une prise car elle doit prendre obligatoirement
        renvoie les coordonnées des pièces pouvant prendre"""
        res = []
        for y in range(10):
            for x in range(10):
                if self.get_color((x, y)) == couleur:
                    piece = Piece((x, y), couleur)
                    if piece.prises_possibles(self.plateau) != []:
                        res.append((x, y))
        return res

    def select(self, pos):
        x, y = pos
        if self.plateau[y][x]:
            # si on clique sur une piece
            self.piece_est_touchee = True
            couleur = self.get_color(pos)
            self.piece_touchee = Piece(pos, couleur)

            if self.plateau[y][x] == couleur * 10:
                self.piece_touchee.est_dame = True

        else:
            # si on clique sur une case vide
            self.deselect()

    def deselect(self):
        self.piece_est_touchee = False
        self.piece_touchee = None

    def enlever(self, pos):
        """retire une pièce du plateau"""
        x, y = pos
        self.plateau[y][x] = 0

    def get_color(self, case):
        x, y = case
        if self.plateau[y][x] < 10:
            return self.plateau[y][x]
        return self.plateau[y][x] // 10

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
                    piece = PIECES[self.plateau[y][x]]  # `piece` est une image
                    piece = pg.transform.scale(piece, (taille, taille))
                    self.win.blit(piece, (x * taille, y * taille))
