from turtle import *

t = Turtle()  # объект (она рисует)
t.shape('turtle')  # форма объекта
t.color('white')  # цвет черепашки

s = Screen()  # холст
s.title('Моя черепашка')  # название окна
s.bgcolor('black')  # фон холста

n = int(input('Количество углов: '))

for line in range(n):
    t.fd(100)  # идти вперед
    t.stamp()  # оставить отпечаток черепашки
    t.bk(100)  # иду назад
    t.rt(360 / n)  # повернуть вправо


done()  # окно не должно закрываться само
