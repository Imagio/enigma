import unittest
from rotor_settings import RotorSettings
from rotor import Rotor


class TestRotorSettings(unittest.TestCase):

    def test_encrypt_A_10(self):
        rotor = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
        settings = RotorSettings(rotor, 10)
        encrypted = settings.encrypt("A")
        self.assertEqual("D", encrypted)

    def test_decrypt_A_10(self):
        rotor = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
        settings = RotorSettings(rotor, 10)
        decrypted = settings.decrypt("A")
        self.assertEqual("R", decrypted)
