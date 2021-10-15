#!/usr/bin/env python3

import pygame as pg
from constants import *

# TODO Prises


class Piece:
    def __init__(self, pos, couleur, dame=False):
        self.x, self.y = pos
        self.couleur = couleur
        self.est_dame = dame

    def coups_possibles(self, plateau):
        """Donne les coups possibles pour la pièce en question"""
        if not self.est_dame:
            if self.couleur == 1:
                # les pièces blanches montent
                res = [(self.x + 1, self.y - 1), (self.x - 1, self.y - 1)]
            if self.couleur == 2:
                # les pièces noires descendent
                res = [(self.x + 1, self.y + 1), (self.x - 1, self.y + 1)]

        return res

    def deplacer(self, plateau, arrivee):
        """déplace la pièce sans se soucier de l'arrivée"""
        x_arr, y_arr = arrivee

        plateau[y_arr][x_arr] = plateau[self.y][self.x]
        plateau[self.y][self.x] = 0

        self.x = x_arr
        self.y = y_arr
