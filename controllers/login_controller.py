from PySide6.QtWidgets import QDialog, QLabel
from views.login_ui import VentanaLogin

class LoginController(QDialog):
    def __init__(self, app, user_service):
        super().__init__()
        self.app = app
        self.service = user_service

        self.ui = VentanaLogin()
        self.ui.setupUi(self)

        self.labelError = QLabel("")
        self.ui.gridLayout.addWidget(self.labelError, 6, 2)

        self.ui.BotonInicioSesion.clicked.connect(self.login)
        self.ui.botonRegistrarse.clicked.connect(self.registro)

    def login(self):
        usuario = self.ui.entradaUsuario.text().strip()
        clave = self.ui.entradaClave.text().strip()

        if not usuario or not clave:
            self.labelError.setText("Debe rellenar todos los campos")
            return

        user = self.service.login(usuario, clave)

        if user:
            self.close()
            self.app.open_menu(user)   # <<--- ESTO ES LO IMPORTANTE
        else:
            self.labelError.setText("Usuario o contraseña incorrectos")

    def registro(self):
        self.close()
        self.app.show_registro()
