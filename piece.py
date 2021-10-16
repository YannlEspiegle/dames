#!/usr/bin/env python3

import pygame as pg
from constants import *


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
                res = [
                    (self.x + 1, self.y - 1),
                    (self.x - 1, self.y - 1),
                ]
            elif self.couleur == 2:
                # les pièces noires descendent
                res = [
                    (self.x + 1, self.y + 1),
                    (self.x - 1, self.y + 1),
                ]

            prises = self.prises_possibles(plateau)
            if prises != []:
                return prises

        return res

    def prises_possibles(self, plateau):
        """un pion peut prendre en vers le haut et le bas"""
        res = []

        if self.couleur == 1:
            adverses = [2, 20]
        else:
            adverses = [1, 10]

        adv_possibles = [  # cases possibles des adversaires
            (self.x + 1, self.y - 1),
            (self.x - 1, self.y - 1),
            (self.x + 1, self.y + 1),
            (self.x - 1, self.y + 1),
        ]

        arrivees_possibles = [
            (self.x + 2, self.y - 2),
            (self.x - 2, self.y - 2),
            (self.x + 2, self.y + 2),
            (self.x - 2, self.y + 2),
        ]

        for i in range(4):
            x, y = adv_possibles[i]

            # on vérifie que l'arrivée est dans le plateau
            arr = arrivees_possibles[i]
            if 0 <= arr[0] < 10 and 0 <= arr[1] < 10:
                # on vérifie que la diagonale est bien un adversaires
                if plateau[y][x] in adverses:
                    res.append(arr)

        return res

    def deplacer(self, plateau, arrivee):
        """déplace la pièce sans se soucier de l'arrivée"""
        x_arr, y_arr = arrivee

        plateau[y_arr][x_arr] = plateau[self.y][self.x]
        plateau[self.y][self.x] = 0

        self.x = x_arr
        self.y = y_arr
