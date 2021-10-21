#!/usr/bin/env python3

import pygame as pg
from constants import *


class Piece:
    def __init__(self, pos, couleur, plateau, dame=False):
        self.x, self.y = pos
        self.couleur = couleur
        self.est_dame = dame
        self.plateau = plateau

    def coups_possibles(self):
        """Donne les coups possibles pour la pièce en question"""

        # si une prise est possibles, il faut la faire obligatoirement
        prises = self.prises_possibles()
        if prises != []:
            return [prise[0] for prise in prises] # on renvoie seulement la case d'arrivée

        if self.est_dame:
            return self.coups_possibles_dame()

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
        return res

    def coups_possibles_dame(self):
        res = []
        for direction in range(4):
            longueur = 1
            x, y = self.diagonale(self.x, self.y, direction, longueur)
            while 0 <= x < 10 and 0 <= y < 10 and self.plateau[y][x] == 0:
                res.append((x, y))
                longueur += 1
                x, y = self.diagonale(self.x, self.y, direction, longueur)

        return res

    def prises_possibles(self):
        """Renvoie les cases d'arrivée des prises possibles par la pièce, ainsi que la case de l'adversaire à enlever"""
        if self.est_dame:
            return self.prises_possibles_dame()

        res = []

        if self.couleur == 1:
            adverses = [2, 20]
        else:
            adverses = [1, 10]

        for direction in range(4):
            adv_x, adv_y = self.diagonale(self.x, self.y, direction, l=1) # case de l'adversaire possibles
            arr_x, arr_y = self.diagonale(self.x, self.y, direction, l=2) # case de l'arrivée

            # on vérifie que l'arrivée est dans le plateau et est vide
            if 0 <= arr_x < 10 and 0 <= arr_y < 10 and self.plateau[arr_y][arr_x] == 0:
                # on vérifie que la diagonale est bien un adversaires
                if self.plateau[adv_y][adv_x] in adverses:
                    res.append([(arr_x, arr_y), (adv_x, adv_y)])
        return res

    def prises_possibles_dame(self):
        res = []

        if self.couleur == 1:
            adverses = [2, 20]
        else:
            adverses = [1, 10]

        for direction in range(4):
            longueur = 1
            x, y = self.diagonale(self.x, self.y, direction, longueur)
            while 0 <= x < 10 and 0 <= y < 10:
                if self.plateau[y][x] != 0:
                    if self.plateau[y][x] in adverses:
                        i = 1
                        # x_arr, y_arr = cases d'arrivée
                        x_arr, y_arr = self.diagonale(self.x, self.y, direction, longueur + i)
                        while 0 <= x_arr < 10 and 0 <= y_arr < 10 and self.plateau[y_arr][x_arr] == 0:
                            res.append([(x_arr, y_arr), (x, y)]) # case d'arrivée puis case de l'adversaire
                            i += 1
                            x_arr, y_arr = self.diagonale(self.x, self.y, direction, longueur + i)

                    break
                else:
                    longueur += 1
                    x, y = self.diagonale(self.x, self.y, direction, longueur)

        return res

    def deplacer(self, arrivee):
        """déplace la pièce sans se soucier de l'arrivée"""
        x_arr, y_arr = arrivee

        self.plateau[y_arr][x_arr] = self.plateau[self.y][self.x]
        self.plateau[self.y][self.x] = 0

        self.x = x_arr
        self.y = y_arr

    def promotion(self):
        if not self.est_dame:
            self.plateau[self.y][self.x] *= 10
        self.est_dame = True

    def diagonale(self, x, y, direction, l):
        """renvoie la case de direction {0, 1, 2, 3} (la vrai direction n'importe pas) et de longueur l"""
        direct = {  # les quatres directions possibles
            0: (x + l, y - l),
            1: (x - l, y - l),
            2: (x + l, y + l),
            3: (x - l, y + l),
        }
        return direct[direction]
