#!/usr/bin/env python3

import pygame as pg

from constants import GREY, HEIGHT, TRUE_BLACK, WHITE, WIDTH
from pictures import (
    TEXTE_EGALITE,
    TEXTE_VICTOIRE_BLANCS,
    TEXTE_VICTOIRE_NOIRS,
    TITRE_COULEUR_BLANC,
    TITRE_COULEUR_NOIR,
)


def draw_endscreen(win, winner):
    # Le titre fait les 2/3 de l'écran
    longueur_titre = 2 * WIDTH // 3
    hauteur_titre = longueur_titre // 2

    if winner == 1:
        # blancs gagnent -> fond blanc, écriture noire
        titre = TITRE_COULEUR_NOIR
        texte = TEXTE_VICTOIRE_BLANCS
        win.fill(WHITE)

    elif winner == 2:
        # noirs gagnent -> fond noir, écriture blanche
        titre = TITRE_COULEUR_BLANC
        texte = TEXTE_VICTOIRE_NOIRS
        win.fill(TRUE_BLACK)

    elif winner == 0:
        # égalité -> fond gris, écriture blanche
        titre = TITRE_COULEUR_BLANC
        texte = TEXTE_EGALITE
        win.fill(GREY)

    # on redimensionne le titre et le texte
    titre = pg.transform.scale(titre, (longueur_titre, hauteur_titre))
    texte = pg.transform.scale(texte, (longueur_titre, hauteur_titre))

    # titre centré -> espacement de 1/6 d'écran
    win.blit(titre, (WIDTH // 6, 40))
    win.blit(texte, (WIDTH // 6, HEIGHT // 2))
