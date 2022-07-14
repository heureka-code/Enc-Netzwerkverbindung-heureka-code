Der Client
==================================

.. autoclass:: enc_netzwerkverbindung.client.CryptoClient
    :members:


>>> from enc_netzwerkverbindung.client import CryptoClient
>>> if __name__ == "__main__":
>>>    c = CryptoClient("127.0.0.1")
>>>    c.send(b"Test")
>>>    antwort = c.receive()
