from turtle import *

t = Turtle()  # объект (она рисует)
t.shape('turtle')  # форма объекта
t.color('white')

s = Screen()  # холст
s.title('Моя черепашка')  # название окна
s.bgcolor('black')  # фон холста

done()  # окно не должно закрываться само
