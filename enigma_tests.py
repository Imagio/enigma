import unittest
from enigma import Enigma
from rotor import Rotor
from rotor_settings import RotorSettings
from reflector import Reflector
from commutator import Commutator


class TestEnigma(unittest.TestCase):

    def test_encrypt_A_rot_1_shift_4_refl_B(self):
        rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", [17])
        reflectorB = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
        commutator = Commutator()
        rotor_settings = RotorSettings(rotor1, 4)

        encryptor = Enigma(reflectorB, [rotor_settings], commutator)
        decryptor = Enigma(reflectorB, [rotor_settings], commutator)

        encrypted = encryptor.encrypt("A")
        self.assertEqual("I", encrypted)

        decrypted = decryptor.encrypt("I")
        self.assertEqual("A", decrypted)

    def test_encrypt_A_rot_1_shift_4_rot_3_shift_2_refl_B(self):
        rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
        rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO")
        reflectorB = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
        commutator = Commutator()
        rotor1_settings = RotorSettings(rotor1, 4)
        rotor3_settings = RotorSettings(rotor3, 2)

        encryptor = Enigma(reflectorB, [rotor1_settings, rotor3_settings], commutator)
        decryptor = Enigma(reflectorB, [rotor1_settings, rotor3_settings], commutator)

        encrypted = encryptor.encrypt("A")
        self.assertEqual("E", encrypted)

        decrypted = decryptor.encrypt("E")
        self.assertEqual("A", decrypted)

    def test_str(self):
        rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", [17])
        rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", [5])
        rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", [22])
        reflectorB = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
        commutator = Commutator("AZ DY")
        r1 = RotorSettings(rotor1, 2)
        r2 = RotorSettings(rotor2, -5)
        r3 = RotorSettings(rotor3, 0)

        enc = Enigma(reflectorB, [r1, r2, r3], commutator)
        dec = Enigma(reflectorB, [r1, r2, r3], commutator)

        s = "Lorem ipsum dolor sit amet"
        encrypted = enc.encrypt(s)
        decrypted = dec.encrypt(encrypted)

        self.assertEqual("LOREMIPSUMDOLORSITAMET", decrypted)
