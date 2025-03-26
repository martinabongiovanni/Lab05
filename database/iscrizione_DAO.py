from database.DB_connect import DBConnect


class iscrizione_DAO:
    def __init__(self):
        self.dbConnect = DBConnect()

    def getIscrizioneDAO(self, matricola, codins):
        '''
        Ricerca l'iscrizione di uno studente a un corso
        :param matricola: matricola di uno studente
        :param codins: codice di un corso
        :return:
        False se non trova un'iscrizione, quindi posso inserirne una nuova
        True se trova un'iscrizione, quindi lo studente è già iscritto al corso
        '''
        cnx = self.dbConnect.get_connection()
        cursor = cnx.cursor()
        query = """
                    SELECT i.*
                    FROM iscrizione i
                    WHERE i.matricola = %s AND i.codins = %s"""
        cursor.execute(query, (matricola, codins))
        row = cursor.fetchall()
        if len(row) == 0:
            return False
        else:
            return True

    def iscrizioneDAO(self, matricola, codins):
        '''
        Inserisce una nuova iscrizione di uno studente a un corso
        :param matricola: matricola di uno studente
        :param codins: codice di un corso
        :return: tupla di matricola dello studente e codice del corso
        '''
        cnx = self.dbConnect.get_connection()
        cursor = cnx.cursor()
        query = """
                    INSERT INTO iscrizione
                    VALUES (%s, %s)"""
        cursor.execute(query, (matricola, codins))
        return (matricola, codins)
