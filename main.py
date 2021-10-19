#!/usr/bin/env python3

import pygame as pg

from constants import FPS, HEIGHT, WHITE, WIDTH
from game import Game

pg.init()

WIN = pg.display.set_mode((WIDTH, HEIGHT))  # la variable représentant la fenêtre
pg.display.set_caption("Jeu de dames")

clock = pg.time.Clock()  # Horloge pour représenter les fps

g = Game(WIN)


def draw():
    g.draw()
    pg.display.update()


def main():
    while True:
        draw()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return 0

            if event.type == pg.MOUSEBUTTONDOWN:
                position = pg.mouse.get_pos()
                g.onclick(position)

            if event.type == pg.KEYDOWN:
                if pg.key.get_mods() & pg.KMOD_CTRL:
                    if event.key == pg.K_a:
                        # Ctrl+a -> abandon
                        g.abandon()
                    elif event.key == pg.K_e:
                        # Ctrl+e -> égalité
                        g.nulle()

        clock.tick(FPS)


if __name__ == "__main__":
    main()
