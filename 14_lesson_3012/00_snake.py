import sys
import pygame as pg


def setup() -> object:
    pg.init()
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)  # окошко открывается на весь экран
    clock = pg.time.Clock()
    return screen, clock


def main(surface: object, updater: object) -> None:
    done = False
    while not done:
        surface.fill(pg.Color('cadetblue1'))
        for event in pg.event.get():
            if (event.type == pg.QUIT) or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                done = True
                sys.exit()  # правильное ЗАКРЫТИЕ окна программы
        pg.display.flip()  # обновление экрана
        updater.tick(60)  # FPS игры


screen, clock = setup()
main(screen, clock)
