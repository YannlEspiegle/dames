#!/usr/bin/env python3

import pygame as pg

PIECES = {
    1: pg.image.load("assets/pion_blanc.png"),
    2: pg.image.load("assets/pion_noir.png"),
    10: pg.image.load("assets/dame_blanche.png"),
    20: pg.image.load("assets/dame_noire.png"),
}

TITRE_COULEUR_BLANC = pg.image.load("assets/titre.png")
TITRE_COULEUR_NOIR = pg.image.load("assets/titre_noir.png")

TEXTE_EGALITE = pg.image.load("assets/egalite.png")
TEXTE_VICTOIRE_BLANCS = pg.image.load("assets/victoire_blanc.png")
TEXTE_VICTOIRE_NOIRS = pg.image.load("assets/victoire_noir.png")
