PHONE_CODES = {
    12: '+',
    11: '+3',
    10: '+38',
    20: '+38',
    22: '+3',
    24: '+',
}


def phone_replace(phone: str) -> str:
    """
    Функция получает номер телефона через параметр
    и, в зависимости от длины строки, добавляет префиксы
    :param phone: str номер телефона
    :return: номер телефона с префиксом
    """
    return PHONE_CODES[len(phone)] + phone

