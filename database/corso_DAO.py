# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import DBConnect
# importa il modello
from model.corso import Corso

class corso_DAO:
    def __init__(self):
        self.dbConnect = DBConnect()

    def getCorsi(self):
        '''
        Ricerca tutti i corsi salvati nel database
        :return: una lista di corsi
        '''
        cnx = self.dbConnect.get_connection()
        cursor = cnx.cursor()
        query = """
                SELECT * 
                FROM corso"""
        cursor.execute(query)

        self._listaCorsi = []
        for row in cursor.fetchall():
            c = Corso(row[0], row[1], row[2], row[3])
            self._listaCorsi.append(c)
        cnx.close()
        return self._listaCorsi

    def getCorsiDelloStudente(self, matricola):
        '''
        Ricerca tutti i corsi a cui è iscritto uno studente
        :param matricola: matricola di uno studente
        :return: lista dei corsi a cui è iscritto lo studente
        '''
        cnx = self.dbConnect.get_connection()
        cursor = cnx.cursor()
        query = """
                SELECT c.* 
                FROM corso c, iscrizione i
                WHERE c.codins = i.codins AND i.matricola = %s"""
        cursor.execute(query, (matricola, ))

        self._listaCorsiDelloStudente = []
        for row in cursor.fetchall():
            c = Corso(row[0], row[1], row[2], row[3])
            self._listaCorsiDelloStudente.append(c)
        cnx.close()
        return self._listaCorsiDelloStudente