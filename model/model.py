from database.corso_DAO import corso_DAO
from database.iscrizione_DAO import iscrizione_DAO
from database.studente_DAO import studente_DAO



class Model:
    def __init__(self):
        self._corsoDAO = corso_DAO()
        self._studenteDAO = studente_DAO()
        self._iscrizioneDAO = iscrizione_DAO()

    def getCorsiDalDAO(self):
        return self._corsoDAO.getCorsi()

    def getStudenteIscrittoAlCorsoDalDAO(self, codins):
        return self._studenteDAO.getStudenteDAOInBaseAlCorso(codins)

    def getStudenteInBaseAllaMatricolaDalDAO(self, matricola):
        return self._studenteDAO.getStudenteDAOInBaseAllaMatricola(matricola)

    def getCorsiDelloStudenteDalDAO(self, matricola):
        return self._corsoDAO.getCorsiDelloStudente(matricola)

    def getIscrizioneDelloStudenteAlCorsoDalDAO(self, matricola, codins):
        return self._iscrizioneDAO.getIscrizioneDAO(matricola, codins)

    def iscrizioneStudenteACorsoInDAO(self, matricola, codins):
        return self._iscrizioneDAO.iscrizioneDAO(matricola, codins)