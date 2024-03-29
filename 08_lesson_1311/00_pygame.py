import pygame as pg
from pygame.draw import *

pg.init()  # инициализация библиотеки

# окошко программы
s = pg.display.set_mode((600, 600))
clock = pg.time.Clock()  # добавление задержки в главный цикл программы


# обновление кадров
pg.display.update()

# главный цикл программы или mainloop
# здесь отслеживаются все события
while True:
    clock.tick(30)  # максимальный FPS, быстрее которого программа работать не будет
    for event in pg.event.get():  # для каждого события
        if event.type == pg.QUIT:  # если действие "закрыть"
            pg.quit()  # остановить работу программы
