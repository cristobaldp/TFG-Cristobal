from PySide6.QtWidgets import QDialog, QLabel
from views.registro_ui import VentanaRegistro

class RegistroController(QDialog):
    def __init__(self, app, user_service, cities_service):
        super().__init__()
        self.app = app
        self.service = user_service
        self.cities = cities_service

        self.ui = VentanaRegistro()
        self.ui.setupUi(self)

        self.labelInfo = QLabel("")
        self.ui.gridLayout.addWidget(self.labelInfo, 20, 3)

        self.ui.comboBoxLocalidad.addItems(self.cities.cargar())

        self.ui.botonCrearCuenta.clicked.connect(self.registrar)
        self.ui.botonVolver.clicked.connect(self.volver)

    def registrar(self):
        nombre = self.ui.entradaNombre.text().strip()
        apellidos = self.ui.entradaApellidos.text().strip()
        username = self.ui.entradaNombreUsuario.text().strip()
        telefono = self.ui.entradaTelefono.text().strip()
        email = self.ui.entradaCorreo.text().strip()
        ciudad = self.ui.comboBoxLocalidad.currentText()
        clave = self.ui.entradaClaveRegistro.text().strip()
        confirmar = self.ui.entradaConfirmarClave.text().strip()
        fecha = self.ui.dateEditEdad.date().toString("yyyy-MM-dd")

        if clave != confirmar:
            self.labelInfo.setText("Las contraseñas no coinciden")
            return

        res = self.service.registrar(
            nombre, apellidos, username, email, telefono, ciudad, fecha, clave
        )

        if res == "OK":
            self.labelInfo.setText("Usuario registrado correctamente")

        elif res == "EMAIL_INVALIDO":
            self.labelInfo.setText("Correo no válido")

        elif res == "TELEFONO_INVALIDO":
            self.labelInfo.setText("Teléfono no válido")

        else:
            self.labelInfo.setText("Error: usuario o email ya existe")

    def volver(self):
        self.app.show_login()
        self.close()
