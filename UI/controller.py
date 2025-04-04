import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillCorsi(self):
        '''
        Riempie il dropDown con la lista di corsi ottenuta dalla ricerca sul database
        :return: aggiorna la view
        '''
        for corso in self._model.getCorsiDalDAO():
            self._view._dd_corso.options.append(ft.dropdown.Option(key = corso._codins, text = corso.__str__()))
        self._view.update_page()

    def handle_inserimentoProibito(self, e):
        '''
        Se si prova a inserire un nome o un cognome viene visualizzato un messaggio di alert.
        :param e:
        :return:
        '''
        self._view.create_alert("Attenzione! Inserire una matricola.")
        self._view._txt_matricola.focus()

    def handle_cercaIscritti(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        corsoScelto = self._view._dd_corso.value
        if corsoScelto is None or corsoScelto == "":
            self._view.create_alert("Selezionare un corso!")
            return
        iscrittiAlCorso = self._model.getStudenteIscrittoAlCorsoDalDAO(corsoScelto)
        self._view.txt_result.controls.clear()
        self._view._txt_matricola.value = ""
        self._view._txt_nome.value = ""
        self._view._txt_cognome.value = ""
        self._view.txt_result.controls.append(ft.Text(f"Ci sono {len(iscrittiAlCorso)} iscritti al corso.",
                                                      italic=True,
                                                      weight=ft.FontWeight.BOLD))
        for i in iscrittiAlCorso:
            self._view.txt_result.controls.append(ft.Text(i))
        self._view.update_page()

    def handle_cercaStudente(self, e):
        matricola = self._view._txt_matricola.value
        studenteTrovato = self._model.getStudenteInBaseAllaMatricolaDalDAO(matricola)
        if matricola is None or matricola == "" or studenteTrovato is None:
            self._view.create_alert("Selezionare un matricola!")
            return
        self._view.txt_result.controls.clear()
        self._view._txt_nome.value = studenteTrovato._nome
        self._view._txt_cognome.value = studenteTrovato._cognome
        self._view._dd_corso.value = ""
        self._view.update_page()

    def handle_cercaCorsi(self, e):
        matricola = self._view._txt_matricola.value
        if matricola is None or matricola == "":
            self._view.create_alert("Selezionare un matricola!")
            return
        listaCorsiDelloStudente = self._model.getCorsiDelloStudenteDalDAO(matricola)
        self._view.txt_result.controls.clear()
        self._view._dd_corso.value = ""
        self._view.txt_result.controls.append(ft.Text(f"Lo studente selezionato è iscritto a {len(listaCorsiDelloStudente)} corsi:",
                                                      italic=True,
                                                      weight=ft.FontWeight.BOLD))
        for c in listaCorsiDelloStudente:
            self._view.txt_result.controls.append(ft.Text(c))
        self._view.update_page()

    def handle_cercaStudenteDelCorso(self, e):
        corsoScelto = self._view._dd_corso.value
        if corsoScelto is None or corsoScelto == "":
            self._view.create_alert("Selezionare un corso!")
            return
        matricola = self._view._txt_matricola.value
        if matricola is None or matricola == "":
            self._view.create_alert("Selezionare un matricola!")
            return


    def handle_iscrivi(self, e):
        corsoScelto = self._view._dd_corso.value
        if corsoScelto is None or corsoScelto == "":
            self._view.create_alert("Selezionare un corso!")
            return
        matricola = self._view._txt_matricola.value
        if matricola is None or matricola == "":
            self._view.create_alert("Selezionare un matricola!")
            self._view._txt_nome.value = ""
            self._view._txt_cognome.value = ""
            self._view.update_page()
            return
        if self._model.getStudenteInBaseAllaMatricolaDalDAO(matricola) is None:
            self._view.create_alert("Attenzione! La matricola inserita è inesistente.")
            self._view._txt_nome.value = ""
            self._view._txt_cognome.value = ""
            self._view.update_page()
            return
        studenteTrovato = self._model.getStudenteInBaseAllaMatricolaDalDAO(matricola)
        self._view._txt_nome.value = studenteTrovato._nome
        self._view._txt_cognome.value = studenteTrovato._cognome
        self._view._dd_corso.value = ""
        self._view.update_page()
        iscrizionePossibile = self._model.getIscrizioneDelloStudenteAlCorsoDalDAO(matricola, corsoScelto)
        if iscrizionePossibile is True:
            self._view.txt_result.controls.clear()
            self._view.create_alert("Lo studente è già iscritto al corso!")
            return
        else:
            nuovaIscrizione = self._model.iscrizioneStudenteACorsoInDAO(matricola, corsoScelto)
            self._view.txt_result.controls.clear()
            row = ft.Row([ft.Text(f"Iscrizione effettuata con successo!",
                                  italic=True,
                                  color = "green",
                                  weight=ft.FontWeight.BOLD),
                          ft.Icon(ft.icons.CHECK_CIRCLE_ROUNDED,
                                  color="green",
                                  size=30)])
            self._view.txt_result.controls.append(row)
            self._view.txt_result.controls.append(ft.Text(f"Lo studente con matricola {matricola} risulta correttamente iscritto al corso con codice {corsoScelto}"))
            self._view.update_page()

