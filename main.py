import common
from rotor import *
from reflector import *
from commutator import *
from enigma import *

ROTOR_DICT = {
    0: Rotor("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
    1: Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", [17]),
    2: Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", [5]),
    3: Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", [22]),
    4: Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", [10]),
    5: Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", [0]),
    6: Rotor("JPGVOUMFYQBENHZRDKASXLICTW", [0, 13]),
    7: Rotor("NZJHGRCXMYSWBOUFAIVLPEKQDT", [0, 13]),
    8: Rotor("FKQHTLXOCBJSPDZRAMEWNIUYGV", [0, 13]),
    "beta": Rotor("LEYJVCNIXWPBQMDRTAKZGFUHOS"),
    "gamma": Rotor("FSOKANUERHMBTIYCWLQPZXVGJD"),
}

REFLECTORS = {
    "A": Reflector("EJMZALYXVBWFCRQUONTSPIKHGD"),
    "B": Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT"),
    "C": Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL"),
    "B Thin": Reflector("ENKQAUYWJICOPBLMDXZVFTHRGS"),
    "C Thin": Reflector("RDOBJNTKVEHMLFCWZAXGYIPSUQ"),
}

machine = Enigma(
    REFLECTORS["B"],
    [
        RotorSettings(ROTOR_DICT[1]),
        RotorSettings(ROTOR_DICT[3], 5),
        RotorSettings(ROTOR_DICT[2], -10),
        RotorSettings(ROTOR_DICT[5], 4)
    ],
    Commutator("")
)

encrypted = machine.encrypt(common.alphabet)
print(encrypted)
