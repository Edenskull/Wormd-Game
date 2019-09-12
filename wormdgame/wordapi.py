import requests
from .timer import timeout


class WordApi:

    basic_time = 0

    @staticmethod
    def get_api_key():
        req = requests.get('https://random-word-api.herokuapp.com/key')
        return req.text

    @staticmethod
    def get_random_word(token, count):
        req = requests.get('https://random-word-api.herokuapp.com/word?key={}&number={}'.format(token, count))
        return req.json()

    @staticmethod
    @timeout(0)
    def compare_words(system_word, sec):
        for index in system_word:
            print("The word is : " + index)
            user_word = input("Type the word : ")
            if not str(user_word).lower() == str(index).lower():
                return False
        return True

