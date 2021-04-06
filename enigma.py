from reflector import Reflector
from rotor_settings import RotorSettings
from typing import *
from common import alphabet


class Enigma(object):
    __rotors: List[RotorSettings] = None
    __reflector: Reflector = None

    def __init__(self, refl: Reflector, rotors: List[RotorSettings]):
        self.__reflector = refl
        self.__rotors = rotors

    def __encrypt_symbol(self, symbol):
        a = symbol
        for rotor in self.__rotors:
            a = rotor.encrypt(a)
        a = self.__reflector.encrypt(a)
        for rotor in reversed(self.__rotors):
            a = rotor.decrypt(a)
        return a

    def __rotate(self):
        is_moved = False
        for rotor in self.__rotors:
            rotor.rotate()
            if not rotor.is_moving():
                break
            is_moved = True
        if is_moved:
            return

        is_moved = False
        for rotor in self.__rotors[1:]:
            if is_moved:
                rotor.rotate()
                is_moved = False
                if rotor.is_moving():
                    is_moved = True
                continue

            if rotor.is_moving_next():
                rotor.rotate()
                is_moved = True

    def encrypt(self, data: str) -> str:
        res = ""
        for ch in data:
            if ch not in alphabet:
                continue
            self.__rotate()
            res += self.__encrypt_symbol(ch)
        return res
