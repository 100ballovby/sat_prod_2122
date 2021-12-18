from aztro_api import fetch_horoscope
from translate_api import translate


lang = input('На каком языке нужен гороскоп? (en|fr|ru|de) ').lower()
sign = input('Введите знак: ').lower()
day = input('Введите день: ').lower()


horo = fetch_horoscope(sign, day)
translated_horo = translate(horo, lang)
print(translated_horo)
