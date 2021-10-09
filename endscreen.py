#!/usr/bin/env python3

import pygame as pg

from constants import HEIGHT, TRUE_BLACK, WHITE, WIDTH

titre_blanc = pg.image.load("assets/titre.png")
texte_blanc = pg.image.load("assets/victoire_noir.png")

titre_noir = pg.image.load("assets/titre_noir.png")
texte_noir = pg.image.load("assets/victoire_blanc.png")


def draw_endscreen(win, winner):
    # Le titre fait les 2/3 de l'écran
    longueur_titre = 2 * WIDTH // 3
    hauteur_titre = longueur_titre // 2

    if winner == 1:
        # blancs gagnent -> fond blanc, écriture noire
        titre = titre_noir
        texte = texte_noir
        win.fill(WHITE)

    elif winner == 2:
        # noirs gagnent -> fond noir, écriture blanche
        titre = titre_blanc
        texte = texte_blanc
        win.fill(TRUE_BLACK)

    # on redimensionne le titre et le texte
    titre = pg.transform.scale(titre, (longueur_titre, hauteur_titre))
    texte = pg.transform.scale(texte, (longueur_titre, hauteur_titre))

    # titre centré -> espacement de 1/6 d'écran
    win.blit(titre, (WIDTH // 6, 40))
    win.blit(texte, (WIDTH // 6, HEIGHT // 2))
