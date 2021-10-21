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
        le deuxième élément renvoyé est vrai si une prise a été efféctuée, faux sinon
        """
        prise = False
        if arrivee in self.piece_touchee.coups_possibles():

            if self.piece_touchee.prises_possibles() != []:
                # prises_possibles renvoie la case d'arrivée puis la case de l'adversaire à supprimer
                for arr, piece_adverse in self.piece_touchee.prises_possibles():
                    if arr == arrivee:
                        self.enlever(piece_adverse)
                prise = True

            self.piece_touchee.deplacer(arrivee)

            # promotions en dames
            if self.piece_touchee.couleur == 1 and arrivee[1] == 0:
                self.piece_touchee.promotion()
            elif self.piece_touchee.couleur == 2 and arrivee[1] == 9:
                self.piece_touchee.promotion()

            return True, prise
        return False, prise

    def pieces_pouvant_prendre(self, couleur):
        """vérifie si une couleur peut faire une prise car elle doit prendre obligatoirement
        renvoie les coordonnées des pièces pouvant prendre"""
        res = []
        for y in range(10):
            for x in range(10):
                if self.get_color((x, y)) == couleur:
                    piece = self.piece_from((x, y))
                    if piece.prises_possibles() != []:
                        res.append((x, y))
        return res

    def select(self, pos):
        """Selectionne la pièce située sur `pos`"""
        x, y = pos
        if self.plateau[y][x]:
            # si on clique sur une piece
            self.piece_est_touchee = True
            self.piece_touchee = self.piece_from(pos)
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

    def get_color(self, pos):
        """Renvoie la couleur de la pièce située sur `pos` (1=blanc, 2=noir)"""
        x, y = pos
        if self.plateau[y][x] < 10:
            return self.plateau[y][x]
        return self.plateau[y][x] // 10

    def liste_pieces(self):
        blancs = []
        noirs = []
        for ligne in self.plateau:
            for piece in ligne:
                if piece:
                    if piece in [1, 10]:
                        blancs.append(piece)
                    else:
                        noirs.append(piece//2)
        return blancs, noirs

    def piece_from(self, pos):
        """Renvoie un objet Piece correspondant à la pièce située sur `pos`"""
        x, y = pos
        couleur = self.get_color(pos)
        est_dame = (self.plateau[y][x] == couleur * 10)
        return Piece(pos, couleur, self.plateau, est_dame)

    def draw(self):
        """dessine le plateau et les pièces sur l'écran"""
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
