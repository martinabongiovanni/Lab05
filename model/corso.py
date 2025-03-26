class Corso:
    def __init__(self, codins, crediti, nome, periodoDidattico):
        self._codins = codins
        self._crediti = crediti
        self._nome = nome
        self._periodoDidattico = periodoDidattico

    def __str__(self):
        return f"{self._nome} ({self._codins})"