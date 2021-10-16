from turtle import *

t = Turtle()  # объект (она рисует)
t.shape('turtle')  # форма объекта
t.color('white')  # цвет черепашки

s = Screen()  # холст
s.title('Моя черепашка')  # название окна
s.bgcolor('black')  # фон холста

t.speed(0)
side = 5
for i in range(400):
    t.fd(side)
    t.lt(90)
    side += 5  # side = side + 5

done()  # окно не должно закрываться само
