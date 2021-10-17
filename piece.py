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
        print(self.coups_possibles_dame(plateau))
        print(self.est_dame)

        # si une prise est possibles, il faut la faire obligatoirement
        prises = self.prises_possibles(plateau)
        if prises != []:
            return prises

        if self.est_dame:
            return self.coups_possibles_dame(plateau)

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

    def coups_possibles_dame(self, plateau):
        res = []
        for direction in range(4):
            longueur = 1
            x, y = self.diagonale(self.x, self.y, direction, longueur)
            while 0 <= x < 10 and 0 <= y < 10 and plateau[y][x] == 0:
                res.append((x, y))
                longueur += 1
                x, y = self.diagonale(self.x, self.y, direction, longueur)

        return res

    def diagonale(self, x, y, direction, l):
        """renvoie la case de direction {0, 1, 2, 3} (la vrai direction n'importe pas) et de longueur l"""
        direct = {  # les quatres directions possibles
            0: (x + l, y - l),
            1: (x - l, y - l),
            2: (x + l, y + l),
            3: (x - l, y + l),
        }
        return direct[direction]

    def prises_possibles(self, plateau):
        """Renvoie les cases d'arrivée des prises possibles par la pièce"""
        res = []

        if self.couleur == 1:
            adverses = [2, 20]
        else:
            adverses = [1, 10]

        # cases possibles des adversaires
        adv_possibles = [
            self.diagonale(self.x, self.y, direction, l=1) for direction in range(4)
        ]

        # cases possibles d'arrivée, càd une case plus loin que l'adversaire
        arrivees_possibles = [
            self.diagonale(self.x, self.y, direction, l=2) for direction in range(4)
        ]

        for i in range(4):
            x, y = adv_possibles[i]
            arr_x, arr_y = arrivees_possibles[i]

            # on vérifie que l'arrivée est dans le plateau et est vide
            if 0 <= arr_x < 10 and 0 <= arr_y < 10 and plateau[arr_y][arr_x] == 0:
                # on vérifie que la diagonale est bien un adversaires
                if plateau[y][x] in adverses:
                    res.append((arr_x, arr_y))

        return res

    def deplacer(self, plateau, arrivee):
        """déplace la pièce sans se soucier de l'arrivée"""
        x_arr, y_arr = arrivee

        plateau[y_arr][x_arr] = plateau[self.y][self.x]
        plateau[self.y][self.x] = 0

        self.x = x_arr
        self.y = y_arr

    def promotion(self, plateau):
        self.est_dame = True
        plateau[self.y][self.x] *= 10
