import pygame as pg
from pygame.draw import *

pg.init()  # инициализация библиотеки

# окошко программы
s = pg.display.set_mode((600, 600))
clock = pg.time.Clock()  # добавление задержки в главный цикл программы

x1, y1, x2, y2 = 50, 50, 280, 250
rect(s, (255, 255, 255), (x1, y1, x2 - x1, y2 - y1), 2)
height = (x2 - x1) // 10
step = x1 + height

for diag in range(10):
    line(s, (255, 255, 255), (step, y1), (step, y2))
    step += height

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