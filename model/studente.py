class Studente:
    def __init__(self, matricola, nome, cognome, corsoDiStudi):
        self._matricola = matricola
        self._nome = nome
        self._cognome = cognome
        self._corsoDiStudi = corsoDiStudi

    def __str__(self):
        return f"{self._nome} {self._cognome} ({self._matricola})"