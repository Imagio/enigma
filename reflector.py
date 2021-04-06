from common import alphabet


class Reflector(object):
    __alphabet: str = None

    def __init__(self, alph: str):
        self.__alphabet = alph

    def encrypt(self, symbol: str) -> str:
        i = alphabet.index(symbol)
        return self.__alphabet[i]
