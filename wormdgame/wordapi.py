import requests


class WordApi:
    @staticmethod
    def get_api_key():
        req = requests.get('https://random-word-api.herokuapp.com/key')
        return req.text

    @staticmethod
    def get_random_word(token, count):
        req = requests.get('https://random-word-api.herokuapp.com/word?key={}&number={}'.format(token, count))
        return req.json()
