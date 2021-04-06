from common import alphabet


class Reflector(object):
    __alphabet: str = None

    def __init__(self, alph):
        self.__alphabet = alph

    def encrypt(self, symbol):
        i = alphabet.index(symbol)
        return self.__alphabet[i]
