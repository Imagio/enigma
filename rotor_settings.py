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
