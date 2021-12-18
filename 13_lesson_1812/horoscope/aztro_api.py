import os
import requests
from requests.exceptions import HTTPError


def fetch_horoscope(sign: str, day: str) -> str or None:
    """
    Connects to the AZTRO API and fetches the horoscope data,
    then returns it to the user
    :param sign: horoscope sign
    :param day: day of horoscope
    :return: the prediction for a sign on a specific day
    """
    url = "https://sameer-kumar-aztro-v1.p.rapidapi.com/"
    headers = {
        'x-rapidapi-host': "sameer-kumar-aztro-v1.p.rapidapi.com",
        'x-rapidapi-key': os.environ.get('API_KEY')
    }
    signs = {
        'овен': 'aries',
        'телец': 'taurus',
        'близнецы': 'gemini',
        'рак': 'cancer',
        'лев': 'leo',
        'дева': 'virgo',
        'весы': 'libra',
        'скорпион': 'scorpio',
        'стрелец': 'sagittarius',
        'козерог': 'capricorn',
        'водолей': 'aquarius',
        'рыбы': 'pisces',
    }
    days = {
        'вчера': 'yesterday',
        'сегодня': 'today',
        'завтра': 'tomorrow',
    }
    try:
        sign = signs[sign]
        day = days[day]

        query = {'sign': sign, 'day': day}  # querystring for server
        response = requests.post(url, headers=headers, params=query)
        json_response = response.json()  # converting response to json object
        horoscope = json_response['description']
        return horoscope  # returning response
    except KeyError:  # dictionary key not found
        print('Вы ввели неправильный знак/день!')
        return None
    except Exception as err:  # something another went wrong
        print(f'Возникла ошибка: {err}')
        return None
    except HTTPError as http_err:  # server connection error
        print(f'Возникла ошибка сервера: {http_err}')
        return None
