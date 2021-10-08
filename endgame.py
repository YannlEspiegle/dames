#!/usr/bin/env python3

import pygame as pg
from constants import BLACK, HEIGHT, WIDTH

titre_blanc = pg.image.load("assets/titre.png")

def draw_endscreen(win):
    longueur_titre = 2 * WIDTH // 3
    hauteur_titre = longueur_titre // 2

    titre_noir = pg.image.load("assets/titre_noir.png")
    titre = pg.transform.scale(titre_noir, (longueur_titre, hauteur_titre))

    win.blit(titre, (WIDTH // 6 , 40))
