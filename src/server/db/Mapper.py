from abc import ABC, abstractmethod
from contextlib import AbstractContextManager

import mysql.connector as connector


class Mapper (AbstractContextManager, ABC):
    """Abstrakte Basisklasse aller Mapper-Klassen"""

    def __init__(self):
        self._cnx = None

    def __enter__(self):

        self._cnx = connector.connect(user='root', password="itprojekt21",
                                      host='34.141.112.201',
                                      database='studi_fix_database')
        """
        self._cnx = connector.connect(user='root', password="root",
                                      host='127.0.0.1',
                                      database='studi_fix')
        """
        """
        self._cnx = connector.connect(user='root', password="itprojekt21",
                                unix_socket='/cloudsql/studifix:europe-west3:studifix-db',
                                database='studi_fix_database')
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Was soll geschehen, wenn wir (evtl. vorübergehend) aufhören, mit dem Mapper zu arbeiten?"""
        self._cnx.close()

    """Formuliere nachfolgend sämtliche Auflagen, die instanzierbare Mapper-Subklassen mid. nerfüllen müssen."""

    @abstractmethod
    def build_bo(self, tuples):
        """Vereinfacht den Bau der bo's in den jeweiligen Mapper"""
        pass

    @abstractmethod
    def find_all(self):
        """Lies alle Tupel aus und gib sie als Objekte zurück."""
        pass

    @abstractmethod
    def find_by_id(self, id):
        """Lies den einen Tupel mit der gegebenen ID (vgl. Primärschlüssel) aus."""
        pass

    @abstractmethod
    def insert(self, object):
        """Füge das folgende Objekt als Datensatz in die DB ein."""
        pass

    @abstractmethod
    def update(self, object):
        """Ein Objekt auf einen bereits in der DB enthaltenen Datensatz abbilden."""
        pass

    @abstractmethod
    def delete(self, object):
        """Den Datensatz, der das gegebene Objekt in der DB repräsentiert löschen."""
        pass