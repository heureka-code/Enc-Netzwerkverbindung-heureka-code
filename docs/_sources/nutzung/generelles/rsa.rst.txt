RSA
========================

Schlüsselgenerierung
----------------------------

.. autoclass:: enc_netzwerkverbindung._generell.RSASchluessel
    :members:


>>> from enc_netzwerkverbindung._generell import RSASchluessel
>>> sk = RSASchluessel.generiere_rsa_schluessel()
>>> pk = RSASchluessel.berechne_oeffentlichen_schluessel(sk)

Verschlüsselt wird allerdings in einer anderen Klasse

Kodierung
-------------------

.. autoclass:: enc_netzwerkverbindung._generell.RSAKodierung
    :members:

>>> from enc_netzwerkverbindung._generell import RSASchluessel, RSAKodierung
>>> sk = RSASchluessel.generiere_rsa_schluessel()
>>> pk = RSASchluessel.berechne_oeffentlichen_schluessel(sk)
>>> msg = b"Test"
>>> c = RSAKodierung.encrypt(pk, msg)
>>> dec = RSAKodierung.decrypt(sk, c)
>>> msg == dec
True

Der Mantel (Serverspezifisch)
--------------------------------

.. _rsaschluesselpaar:

Um die Herkunft des RSA-Schlüssels beeinflussen zu können, wird eine abstrakte Klasse definiert.


.. autoclass:: enc_netzwerkverbindung.server.RSASchluesselpaar
    :members:

    .. automethod:: enc_netzwerkverbindung.server.RSASchluesselpaar._setup

    Muss implementiert werden und liefert einen privaten RSA-Schlüssel, der für die Verbindung verwendet werden soll

Standard ist eine Unterklasse, die bei jedem Serverstart einen neuen Schlüssel erzeugt.


