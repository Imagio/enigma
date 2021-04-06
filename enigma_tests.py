import unittest
from enigma import Enigma
from rotor import Rotor
from rotor_settings import RotorSettings
from reflector import Reflector

class TestEnigma(unittest.TestCase):

    def test_encrypt_A_rot_1_shift_5_refl_B(self):
        rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
        reflectorB = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
        rotor1_settings = RotorSettings(rotor1, 5)
        enigma = Enigma(reflectorB, [rotor1_settings])

        encrypted = enigma.encrypt("A")
        self.assertEqual("I", encrypted)

        decrypted = enigma.encrypt("I")
        self.assertEqual("A", decrypted)

    def test_encrypt_A_rot_1_shift_5_rot_3_shift_2_refl_B(self):
        rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
        rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO")
        reflectorB = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
        rotor1_settings = RotorSettings(rotor1, 5)
        rotor3_settings = RotorSettings(rotor3, 2)
        enigma = Enigma(reflectorB, [rotor1_settings, rotor3_settings])

        encrypted = enigma.encrypt("A")
        self.assertEqual("E", encrypted)

        decrypted = enigma.encrypt("E")
        self.assertEqual("A", decrypted)
