def foo(a, b):
    a *= a ** 2 ** 2
    b -= a
    return a, b

_, res = foo(2, 5)
print(res)
"""
_ <- означает, что переменная в коде использована не будет.
их называют безымянными переменными
"""


class GodObject:

    def _get_inventory(self, player):
        """Функция позволяет игре получить инвентарь игрока"""
        if player is not None:
            inventory = 298570293
        return inventory

    def __ya_incapsulirovan(self):
        return 'lol'

go = GodObject()
go.__ya_incapsulirovan()

"""До класса ставится 2 пустые строки. Функции класса 
разделяются пустыми строками"""
