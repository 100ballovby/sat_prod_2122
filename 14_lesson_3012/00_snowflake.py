import sys
import pygame as pg
import random as r
from pygame.draw import circle


def setup() -> object:
    pg.init()
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)  # окошко открывается на весь экран
    clock = pg.time.Clock()
    return screen, clock


def main(surface: object, updater: object) -> None:
    done = False
    snowflakes = []
    for i in range(500):  # рисую много снежинок
        x = r.randint(0, surface.get_width())
        y = r.randint(0, surface.get_height())
        snowflakes.append((x, y))

    while not done:
        surface.fill(pg.Color('cadetblue1'))
        for event in pg.event.get():
            if (event.type == pg.QUIT) or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                done = True
                sys.exit()  # правильное ЗАКРЫТИЕ окна программы
        for sf in snowflakes:
            circle(surface, pg.Color('snow1'), (sf[0], sf[1]), r.randint(2, 6))  # размер каждой снежинки меняется
        pg.display.flip()  # обновление экрана
        updater.tick(60)  # FPS игры


screen, clock = setup()
main(screen, clock)
