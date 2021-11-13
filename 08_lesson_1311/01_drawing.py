import pygame as pg
from pygame.draw import *

pg.init()  # инициализация библиотеки

# окошко программы
s = pg.display.set_mode((600, 600))
clock = pg.time.Clock()  # добавление задержки в главный цикл программы

rect(s, (0, 210, 178), (100, 100, 200, 200))
rect(s, (0, 0, 255), (100, 100, 200, 200), 6)

circle(s, (225, 229, 242), (100, 175), 50)
circle(s, (255, 0, 0), (100, 175), 50, 5)

# обновление кадров
pg.display.update()

finished = False  # флаговая переменная для работы главного цикла
# главный цикл программы или mainloop
# здесь отслеживаются все события
while not finished:
    clock.tick(30)  # максимальный FPS, быстрее которого программа работать не будет
    for event in pg.event.get():  # для каждого события
        if event.type == pg.QUIT:  # если действие "закрыть"
            finished = True  # остановить работу программы

pg.quit()