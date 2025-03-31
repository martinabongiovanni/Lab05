# Add whatever it is needed to interface with the DB Table studente
from flet_core import row
from model.studente import Studente
from database.DB_connect import DBConnect


class studente_DAO:
    def __init__(self):
        self.dbConnect = DBConnect()

    def getStudenteDAOInBaseAlCorso(self, codins):
        '''
        Ricerca tutti gli studenti iscritto a un corso.
        :param codins: codice del corso di cui si vuole conoscere il numero di iscritti
        :return: lista di studenti
        '''
        cnx = self.dbConnect.get_connection()
        cursor = cnx.cursor()
        query = """
                SELECT s.*
                FROM studente s, iscrizione i
                WHERE s.matricola = i.matricola AND i.codins = %s"""
        cursor.execute(query, (codins, ))

        self._listaStudentiIscrittiAlCorso = []
        for row in cursor.fetchall():
            s = Studente(row[0], row[1], row[2], row[3])
            self._listaStudentiIscrittiAlCorso.append(s)
        cnx.close()
        return self._listaStudentiIscrittiAlCorso

    def getStudenteDAOInBaseAllaMatricola(self, matricola):
        '''
        Ricerca di uno studente
        :param matricola: matricola dello studente da cercare
        :return: si visualizzerà nell'interfaccia nome e cognome dello studente trovato
        '''
        cnx = self.dbConnect.get_connection()
        cursor = cnx.cursor()
        query = """
                        SELECT *
                        FROM studente s
                        WHERE s.matricola = %s"""
        cursor.execute(query, (matricola,))
        row = cursor.fetchone()
        if row is None:
            cnx.close()
            return None
        else:
            studenteTrovato = Studente(row[0], row[1], row[2], row[3])
            cnx.close()
            return studenteTrovato

