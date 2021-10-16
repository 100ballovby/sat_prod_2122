from turtle import *

t = Turtle()  # объект (она рисует)
t.shape('turtle')  # форма объекта
t.color('white')  # цвет черепашки

s = Screen()  # холст
s.title('Моя черепашка')  # название окна
s.bgcolor('black')  # фон холста

# квадрат
for line in range(4):
    t.fd(100)  # идти вперед
    t.rt(90)  # повернуть на 90

done()  # окно не должно закрываться само
