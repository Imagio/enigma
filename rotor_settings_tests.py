import unittest
from rotor_settings import RotorSettings
from rotor_state import RotorState
from rotor import Rotor


class TestRotorSettings(unittest.TestCase):

    def test_encrypt_A_10(self):
        rotor = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
        settings = RotorSettings(rotor, 10)
        state = RotorState(settings)
        encrypted = state.encrypt("A")
        self.assertEqual("D", encrypted)

    def test_decrypt_A_10(self):
        rotor = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
        settings = RotorSettings(rotor, 10)
        state = RotorState(settings)
        decrypted = state.decrypt("A")
        self.assertEqual("R", decrypted)
