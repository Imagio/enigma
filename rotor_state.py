from rotor import Rotor
from rotor_settings import RotorSettings
from common import alphabet


class RotorState(object):
    __rotor: Rotor = None
    __shift: int = None

    def __init__(self, setting: RotorSettings):
        self.__rotor = setting.rotor
        self.__shift = setting.shift

    @staticmethod
    def shift(symbol: str, symbol_shift: int) -> str:
        i = alphabet.index(symbol)
        i += symbol_shift
        i %= len(alphabet)
        return alphabet[i]

    def encrypt(self, symbol: str) -> str:
        before = RotorState.shift(symbol, self.__shift)
        after = self.__rotor.encrypt(before)
        return RotorState.shift(after, -self.__shift)

    def decrypt(self, symbol: str) -> str:
        before = RotorState.shift(symbol, self.__shift)
        after = self.__rotor.decrypt(before)
        return RotorState.shift(after, -self.__shift)

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
