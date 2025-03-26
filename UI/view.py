import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._theme_switch = None
        # prima riga:
        self._dd_corso = None
        self._btn_cercaIscritti = None
        # seconda riga:
        self._txt_matricola = None
        self._txt_nome = None
        self._txt_cognome = None
        # terza riga:
        self._btn_cercaStudente = None
        self._btn_cercaCorsi = None
        self._btn_iscrivi = None

        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        row0 = ft.Row(spacing=120, controls=[self._theme_switch, self._title],
                   alignment=ft.MainAxisAlignment.START)
        self._page.controls.append(row0)

        #ROW with some controls
        # PRIMA RIGA:
        # drop down per selezionare un corso tra quelli presenti nel database
        self._dd_corso = ft.Dropdown(
            label="Corso",
            width=550,
            hint_text="Selezionare un corso"
        )
        self._controller.fillCorsi()

        # button per cercare gli iscritti al corso selezionato
        self._btn_cercaIscritti = ft.ElevatedButton(text="Cerca Iscritti",
                                                    on_click=self._controller.handle_cercaIscritti,
                                                    tooltip="Cerca tutti gli studenti iscritti al corso selezionato.")
        row1 = ft.Row([self._dd_corso, self._btn_cercaIscritti],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # SECONDA RIGA:
        # text field per inserire un numero di matricola
        self._txt_matricola = ft.TextField(
            label="Matricola",
            width=150,
            hint_text="Inserire numero di matricola"
        )
        # text field per inserire un nome
        self._txt_nome = ft.TextField(
            label="Nome",
            width=250,
            read_only=True,
            on_focus=self._controller.handle_inserimentoProibito
        )
        # text field per inserire un cognome
        self._txt_cognome = ft.TextField(
            label="Cognome",
            width=250,
            read_only=True,
            on_focus=self._controller.handle_inserimentoProibito
        )
        row2 = ft.Row([self._txt_matricola, self._txt_nome, self._txt_cognome],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # TERZA RIGA:
        self._btn_cercaStudente = ft.ElevatedButton(text="Cerca Studente",
                                                    on_click=self._controller.handle_cercaStudente,
                                                    tooltip="Verifica se c'è uno studente con la matricola inserita.")
        self._btn_cercaCorsi = ft.ElevatedButton(text="Cerca Corsi",
                                                 on_click=self._controller.handle_cercaCorsi,
                                                 tooltip="Ricerca dei corsi a cui è iscritto lo studente con la matricola inserita.")
        self._btn_iscrivi = ft.ElevatedButton(text="Iscrivi",
                                              on_click=self._controller.handle_iscrivi,
                                              tooltip="Iscrive lo studente con la matricola inserita al corso selezionato.")
        row3 = ft.Row([self._btn_cercaStudente, self._btn_cercaCorsi, self._btn_iscrivi],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)
        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self._page.theme_mode = (
            ft.ThemeMode.DARK
            if self._page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self._theme_switch.label = (
            "Light theme" if self._page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )

        self._page.update()
