Netzwerkverbindung
==============================================

Basisklasse
--------------------

Für Klassen, über die gesendet und empfangen werden kann, wird eine abstrakte Basisklasse erstellt.

.. autoclass:: enc_netzwerkverbindung._generell.verbindung.BasisCOM
    :members:

EncVerbindung
-------------------
Eine Implementierung der Basisklasse verwendet AES für eine verschlüsselte Verbindung.

.. autoclass:: enc_netzwerkverbindung._generell.EncVerbindung
    :members:

Sockets
-------------
Um die für Client und Server verschiedene Verwendung von Sockets zu abstrahieren werden zusätzlich zwei Klassen implementiert.

Client
-------------
Für den Client gibt es eine Implementierung, die den Socket verwaltet.
Die Nachrichten werden hierbei allerdings nicht verschlüsselt.

.. autoclass:: enc_netzwerkverbindung._generell.verbindung.ClientVerbindungsVerwalter
    :members:

Server
--------------
Das Gegenstück zum eben gezeigten. Auch hier wird (noch) nicht verschlüsselt.

.. autoclass:: enc_netzwerkverbindung._generell.verbindung.ServerVerbindungsVerwalter
    :members:

IP-Adresse
-------------
Für das Abrufen der IP-Adresse findet sich hier auch eine Funktion.

.. autofunction:: enc_netzwerkverbindung._generell.get_ip
