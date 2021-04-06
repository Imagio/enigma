import unittest
from enigma import Enigma
from rotor import Rotor
from rotor_settings import RotorSettings
from reflector import Reflector

class TestEnigma(unittest.TestCase):

    def test_encrypt_A_rot_1_shift_4_refl_B(self):
        rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", [17])
        reflectorB = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")

        encryptor_rotor1_settings = RotorSettings(rotor1, 4)
        encryptor = Enigma(reflectorB, [encryptor_rotor1_settings])

        decryptor_rotor1_settings = RotorSettings(rotor1, 4)
        decryptor = Enigma(reflectorB, [decryptor_rotor1_settings])

        encrypted = encryptor.encrypt("A")
        self.assertEqual("I", encrypted)

        decrypted = decryptor.encrypt("I")
        self.assertEqual("A", decrypted)

    def test_encrypt_A_rot_1_shift_4_rot_3_shift_2_refl_B(self):
        rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
        rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO")
        reflectorB = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")

        rotor1_settings = RotorSettings(rotor1, 4)
        rotor3_settings = RotorSettings(rotor3, 2)
        encryptor = Enigma(reflectorB, [rotor1_settings, rotor3_settings])

        rotor1_settings = RotorSettings(rotor1, 4)
        rotor3_settings = RotorSettings(rotor3, 2)
        decryptor = Enigma(reflectorB, [rotor1_settings, rotor3_settings])

        encrypted = encryptor.encrypt("A")
        self.assertEqual("E", encrypted)

        decrypted = decryptor.encrypt("E")
        self.assertEqual("A", decrypted)
