def cows(number: int) -> str:
    word = 'коров'
    if number % 10 == 1:
        completion = 'а'
    elif number in range(4, 21):
        completion = ''
    elif number % 10 in range(2, 4):
        completion = 'ы'
    else:
        completion = ''
    return word + completion

print(cows(12))
"""
1 - коровА 
2-3 - коровЫ
4-20 - коров_ 
"""

