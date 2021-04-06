from rotor import Rotor


class RotorSettings(object):
    __rotor: Rotor = None
    __shift: int = None

    def __init__(self, rotor: Rotor, shift: int):
        self.__rotor = rotor
        self.__shift = shift

    def get_rotor(self):
        return self.__rotor

    def get_shift(self):
        return self.__shift

    rotor = property(get_rotor)
    shift = property(get_shift)
