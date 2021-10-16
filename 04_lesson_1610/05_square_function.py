from turtle import *


def square():
    t.down()  # Опустить перо
    for i in range(4):
        t.fd(100)
        t.rt(90)
    t.up()  # поднять перо

t = Turtle()  # объект (она рисует)
t.shape('turtle')  # форма объекта
t.color('white')  # цвет черепашки

s = Screen()  # холст
s.title('Моя черепашка')  # название окна
s.bgcolor('black')  # фон холста

for i in range(10):
    from random import randint
    square()
    t.goto(randint(-400, 200), randint(-400, 200))


done()  # окно не должно закрываться само
