import math  # включаю библиотеку в свой проект

z = 16
print(math.sqrt(z))  # обращение к библиотеке math, вызов функции v

'''
* import <library> -> обращаюсь к библиотеке. 
чтобы обратиться к функции из библиотеки, я пишу: <library>.function()

* import <library> as <alias> -> создаю библиотеке псевдоним
чтобы обратиться к функции из библиотеки, я пишу <alias>.function()
import math as m -> m.sqrt()

* from <library> import function1, function2, ..., functionN
из библиотеки импортировать определенные функции 
from math import sqrt
sqrt(49) -> 7.0

* from <library> import * - импортировать все 

'''