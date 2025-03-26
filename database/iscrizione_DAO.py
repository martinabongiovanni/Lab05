from database.DB_connect import DBConnect


class iscrizione_DAO:
    def __init__(self):
        self.dbConnect = DBConnect()

    def getIscrizioneDAO(self, matricola, codins):
        cnx = self.dbConnect.get_connection()
        cursor = cnx.cursor()
        query = """
                    SELECT i.*
                    FROM iscrizione i
                    WHERE i.matricola = %s AND i.codins = %s"""
        cursor.execute(query, (matricola, codins))
        row = cursor.fetchall()
        if len(row) == 0:
            return False # posso inserire un nuova iscrizione
        else:
            return True # lo studente è già iscritto al corso

    def iscrizioneDAO(self, matricola, codins):
        cnx = self.dbConnect.get_connection()
        cursor = cnx.cursor()
        query = """
                    INSERT INTO iscrizione
                    VALUES (%s, %s)"""
        cursor.execute(query, (matricola, codins))
        return (matricola, codins)
