AES
========================

Schlüsselgenerierung
----------------------------

.. autoclass:: enc_netzwerkverbindung._generell.AESSchluessel
    :members:


>>> from enc_netzwerkverbindung._generell import AESSchluessel
>>> key = AESSchluessel.generiere_aes_schluessel()
>>> AESSchluessel.CHARS
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
>>> # Die Länge des zu erstellenden Passworts (Defaultwert)
>>> AESSchluessel.KEY_LEN
139
>>> # Der eigentliche Schlüssel ist allerdings gehasht und hat eine feste Länge
>>> len(key)
32

Verschlüsselt wird allerdings in einer anderen Klasse

Kodierung
-------------------

.. autoclass:: enc_netzwerkverbindung._generell.AESKodierung
    :members:

>>> from enc_netzwerkverbindung._generell import AESSchluessel, AESKodierung
>>> key = AESSchluessel.generiere_aes_schluessel()
>>> msg = b"Test"
>>> cipher = AESKodierung(key)
>>> c = cipher.encrypt(msg)
>>> dec = cipher.decrypt(c)
>>> msg == dec
True