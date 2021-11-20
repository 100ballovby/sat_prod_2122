import pygame as pg
import pygame.draw as dr
import sys

colors = {
    'yellow': (255, 224, 18),
    'red': (255, 18, 18),
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'baby-blue': (141, 241, 255),
    'green': (57, 191, 62),
}

pg.init()
s = pg.display.set_mode((400, 400))
clock = pg.time.Clock()

# drawing background
dr.rect(s, colors['baby-blue'], (0, 0, 400, 300))
dr.rect(s, colors['green'], (0, 250, 400, 300))

# drawing house
dr.rect(s, colors['yellow'], (140, 150, 130, 140))
# drawing roof
dr.polygon(s, colors['red'], [[130, 150], [205, 100], [280, 150]])
# drawing door for dead inside
dr.rect(s, colors['white'], (190, 180, 30, 50))

# drawing smoke
dr.circle(s, colors['white'], (70, 50), 20)
dr.circle(s, colors['white'], (90, 50), 20)
dr.circle(s, colors['white'], (100, 75), 20)
dr.circle(s, colors['white'], (125, 95), 20)
dr.circle(s, colors['white'], (145, 115), 20)

pg.display.update()
finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
            sys.exit()
