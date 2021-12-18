import os
import requests
from requests.exceptions import HTTPError


def translate(text: str, lang: str) -> str or None:
    """
        Translates text passed through parameters from english into another language.
        :param query:  text to translate
        :param language: target language of translation
        :return: translated text
        """
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    payload = f"q={text}&target={lang}&source=en"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'accept-encoding': "application/gzip",
        'x-rapidapi-host': "google-translate1.p.rapidapi.com",
        'x-rapidapi-key': os.environ.get('API_KEY')
    }
    try:
        response = requests.post(url, data=payload, headers=headers)
        json_response = response.json()
        translated = json_response['data']['translations'][0]['translatedText']
        return translated
    except Exception as err:  # something another went wrong
        print(f'Возникла ошибка: {err}')
        return None
    except HTTPError as http_err:  # server connection error
        print(f'Возникла ошибка сервера: {http_err}')
        return None

print(translate('Hey! I am hungry', 'ru'))