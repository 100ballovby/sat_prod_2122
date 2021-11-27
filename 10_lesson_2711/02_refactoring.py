def phone_replace_before_refacor(tel):
    if len(tel) == 12:
        num = '+' + tel
    elif len(tel) == 11:
        num = '+3' + tel
    elif len(tel) == 10:
        num = '+38' + tel

    elif len(tel) == 20:
        num = '+38' + tel[:10]
    elif len(tel) == 22:
        num = '+3' + tel[:11]
    elif len(tel) == 24:
        num = '+' + tel[:12]

    return num

PHONE_CODES = {
    12: '+',
    11: '+3',
    10: '+38',
    20: '+38',
    22: '+3',
    24: '+',
}


def phone_replace(phone):
    return PHONE_CODES[len(phone)] + phone

print(phone_replace('0671112999'))
