from typing import *


class Commutator(object):
    __replace: Dict[str, str] = None

    def __init__(self, pairs: str = ""):

        self.__replace = {}

        for pair in pairs.split():
            c1 = pair[0].upper()
            c2 = pair[1].upper()
            self.__replace[c1] = c2
            self.__replace[c2] = c1

    def replace(self, symbol):
        if symbol in self.__replace:
            return self.__replace[symbol]
        return symbol
