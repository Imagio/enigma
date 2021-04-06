from typing import *
import common


class Rotor(object):
    __alphabet: str = None
    __moves: List[int] = None
    __loops: List[str] = None

    def __init__(self, alphabet: str, moves: List[int] = None):
        if moves is None:
            moves = []

        self.__alphabet = alphabet
        self.__moves = moves
        letters = set(common.alphabet)
        self.__loops = []
        while len(letters) > 0:
            first = sorted(list(letters))[0]
            loop = first
            letters.remove(first)
            i = common.alphabet.index(first)
            ch = alphabet[i]
            while first != ch:
                loop += ch
                letters.remove(ch)
                i = common.alphabet.index(ch)
                ch = alphabet[i]
            self.__loops.append(loop)

    def encrypt(self, symbol: str) -> str:
        for loop in self.__loops:
            if symbol in loop:
                i = loop.index(symbol)
                i += 1
                i = i % len(loop)
                return loop[i]
        return symbol

    def decrypt(self, symbol: str) -> str:
        for loop in self.__loops:
            if symbol in loop:
                i = loop.index(symbol)
                i -= 1
                i = i % len(loop)
                return loop[i]
        return symbol
