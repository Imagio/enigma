from rotor import *

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
