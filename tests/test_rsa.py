import unittest

from hypothesis import example, given
from hypothesis import strategies as st

from enc_netzwerkverbindung_heureka_code._generell import (RSAKodierung,
                                                           RSASchluessel)


class TestRSA(unittest.TestCase):
    """ Testet die Implementierung von RSA """
    def setUp(self) -> None:
        """ Erstellt ein neues Schluesselpaar """
        self.sk = RSASchluessel.generiere_rsa_schluessel()
        self.pk = RSASchluessel.berechne_oeffentlichen_schluessel(self.sk)
        pass

    @example(b"\n")
    @example(b"")
    @given(msg=st.binary())
    def test_enc_dec(self, msg: bytes):
        """ Testet die Implementierung von RSA """
        enc = RSAKodierung.encrypt(self.pk, msg)
        dec = RSAKodierung.decrypt(self.sk, enc)
        self.assertEqual(msg, dec)


if __name__ == '__main__':
    unittest.main()
