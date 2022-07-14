Der Server
===============

.. autoclass:: enc_netzwerkverbindung.server.SocketServer
    :members:


Anpassung
==============

Um den Server zu starten, wird ein Kontext erzeugt und übergeben.
Dieser Kontext bietet verschiedene Möglichkeiten der Anpassung.
Um einen neuen Kontext zu erzeugen wird von einer abstrakten Klasse geerbt.

Der Kontext
------------

.. autoclass:: enc_netzwerkverbindung.server.ServerKontext
    :members:

Der ClientHandler
-------------------

Für die Verwaltung eingehender Clientverbindungen muss von einer abstrakten Klasse abgeleitet werden.

.. autoclass:: enc_netzwerkverbindung.server.BasisClientHandler
    :members:

>>> from enc_netzwerkverbindung.server import BasisClientHandler
>>> class Client(BasisClientHandler):
>>>    def verbindung_verwalten(self):
>>>        print(self.verbindung.receive())
>>>        self.verbindung.send(b"Antwort")

Das Schlüsselpaar
---------------------

Die Art und Weise, wie der RSA-Schlüssel erzeugt wird, muss nicht unbedingt angepasst werden.

Bei der Initialisierung der Basisklasse muss ein Objekt einer von :ref:`RSA-Schlüsselpaar <rsaschluesselpaar>` abgeleiteten Klasse als Parameter übergeben werden.

Logging - Server
------------------

.. autoclass:: enc_netzwerkverbindung.server.ServerInfo
    :members:

Im Kontext muss ``get_server_logger`` überschrieben werden, welches einen Logger erstellt.

Logging - Client
------------------

.. autoclass:: enc_netzwerkverbindung.server.ClientInfo
    :members:

Im Kontext muss ``get_client_logger`` überschrieben werden, welches einen Logger erstellt.


Ein Beispielkontext
------------------------

>>> from logging import getLogger, Logger, LoggerAdapter
>>> from enc_netzwerkverbindung.server import ClientInfo, ServerInfo, ServerKontext
>>> class Kontext(ServerKontext):
>>>     def __init__(self, client_handler):
>>>         super(Kontext, self).__init__(client_handler)
>>>
>>>     def get_server_logger(self, server: "ServerInfo") -> ["Logger", "LoggerAdapter"]:
>>>         return getLogger(server.file__name__)
>>>
>>>     def get_client_logger(self, client: "ClientInfo") -> ["Logger", "LoggerAdapter"]:
>>>         return getLogger(client.file__name__)

Mit anderer RSA-Variante
-------------------------

>>> from logging import getLogger, Logger, LoggerAdapter
>>> from enc_netzwerkverbindung.server import ClientInfo, ServerInfo, ServerKontext
>>>
>>> from enc_netzwerkverbindung.server import BasisClientHandler
>>> class Client(BasisClientHandler):
>>>    def verbindung_verwalten(self):
>>>        print(self.verbindung.receive())
>>>        self.verbindung.send(b"Antwort")
>>>
>>> from enc_netzwerkverbindung.server import RSASchluesselpaar
>>> from Crypto.PublicKey import RSA
>>> class RSAVariante(RSASchluesselpaar):
>>>     def _setup(self) -> RsaKey:
>>>         # Der Standardwert ist sowieso 4096
>>>         return RSA.generate(4096)
>>>
>>> class Kontext(ServerKontext):
>>>     def __init__(self, client_handler):
>>>         super(Kontext, self).__init__(client_handler, RSAVariante())
>>>
>>>     def get_server_logger(self, server: "ServerInfo") -> ["Logger", "LoggerAdapter"]:
>>>         return getLogger(server.file__name__)
>>>
>>>     def get_client_logger(self, client: "ClientInfo") -> ["Logger", "LoggerAdapter"]:
>>>         return getLogger(client.file__name__)
>>>
>>> from enc_netzwerkverbindung.server import SocketServer
>>> kontext = Kontext(Client)
>>> server = SocketServer()
>>> server.start(kontext)
