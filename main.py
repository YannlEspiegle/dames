#!/usr/bin/env python3

import pygame as pg

from game import Game
from constants import FPS, HEIGHT, WHITE, WIDTH

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
                print("a")
                p = pg.mouse.get_pos()
                print("b")
                g.onclick(p)

        clock.tick(FPS)


if __name__ == "__main__":
    main()
