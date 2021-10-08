#!/usr/bin/env python3

import pygame as pg

from board import Board
from constants import FPS, HEIGHT, WHITE, WIDTH
from endgame import draw_endscreen

pg.init()

WIN = pg.display.set_mode((WIDTH, HEIGHT))  # la variable représentant la fenêtre
pg.display.set_caption("Jeu de dames")

clock = pg.time.Clock()  # Horloge pour représenter les fps

b = Board(WIN)

def draw():
    WIN.fill(WHITE)
    b.draw()
    #draw_endscreen(WIN)
    pg.display.update()


def main():
    while True:
        clock.tick(FPS)
        draw()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return 0


if __name__ == "__main__":
    main()
