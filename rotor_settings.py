from rotor import Rotor
from common import alphabet


class RotorSettings(object):
    __rotor: Rotor = None
    __shift: int = None

    def __init__(self, rotor: Rotor, shift: int):
        self.__rotor = rotor
        self.__shift = shift

    @staticmethod
    def shift(symbol: str, symbol_shift: int) -> str:
        i = alphabet.index(symbol)
        i += symbol_shift
        i %= len(alphabet)
        return alphabet[i]

    def encrypt(self, symbol: str) -> str:
        before = RotorSettings.shift(symbol, self.__shift)
        after = self.__rotor.encrypt(before)
        return RotorSettings.shift(after, -self.__shift)

    def decrypt(self, symbol: str) -> str:
        before = RotorSettings.shift(symbol, self.__shift)
        after = self.__rotor.decrypt(before)
        return RotorSettings.shift(after, -self.__shift)

    def rotate(self):
        self.__shift += 1
        self.__shift %= len(alphabet)

    def is_moving(self):
        shift = self.__shift
        moves = self.__rotor.moves
        return shift in moves

    def is_moving_next(self):
        shift = self.__shift
        moves = self.__rotor.moves
        shift += 1
        shift %= len(alphabet)
        return shift in moves
