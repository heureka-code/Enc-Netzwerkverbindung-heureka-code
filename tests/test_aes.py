import unittest

from hypothesis import example, given
from hypothesis import strategies as st

from enc_netzwerkverbindung_heureka_code._generell import (AESKodierung,
                                                           AESSchluessel)


class TestAES(unittest.TestCase):
    """ Testet die Implementierung von AES """
    def setUp(self) -> None:
        """ Generiert einen neuen Schluessel """
        self.key = AESSchluessel.generiere_aes_schluessel()
        pass

    def test_laenge(self):
        """ Prueft, ob der Schluessel die richtige Laenge hat """
        self.assertEqual(32, len(self.key))

    @example(b"\n")
    @example(b"")
    @given(msg=st.binary())
    def test_enc_dec(self, msg: bytes):
        """ Prueft, ob richtig Ver- und Entschluesselt wird """
        cipher = AESKodierung(self.key)
        enc = cipher.encrypt(msg)
        dec = cipher.decrypt(enc)
        self.assertEqual(msg, dec)


if __name__ == '__main__':
    unittest.main()
