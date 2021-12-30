import sys
import pygame as pg
import random as r
from pygame.draw import circle, rect


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
        surface.fill(pg.Color('lightblue'))
        for event in pg.event.get():
            if (event.type == pg.QUIT) or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                done = True
                sys.exit()  # правильное ЗАКРЫТИЕ окна программы

        # ground
        rect(surface, pg.Color('snow'), (0, 0.75 * surface.get_height(),
                                          surface.get_width(), 0.25 * surface.get_height()))

        # snowman
        snowman_y = 0.5 * surface.get_height()
        snowman_x = 0.3 * surface.get_width()
        rect(surface, pg.Color('red'), (snowman_x - 20, snowman_y - 50, 40, 42))
        for i in range(1, 4):
            circle(surface, pg.Color('snow'), (snowman_x, snowman_y), i * 30)
            snowman_y += i * 70

        for i in range(len(snowflakes)):
            sf = snowflakes[i]
            snowflakes[i] = (sf[0] + r.randint(-1, 1), sf[1] + r.randint(1, 3))
            circle(surface, pg.Color('snow2'), (sf[0], sf[1]), r.randint(2, 6))  # размер каждой снежинки меняется
            if sf[1] > surface.get_height():  # если y снежинки больше высоты экрана
                snowflakes[i] = (sf[0], 0)  # не трогаем x и перемещаем снежинку наверх
        pg.display.flip()  # обновление экрана
        updater.tick(60)  # FPS игры


screen, clock = setup()
main(screen, clock)
