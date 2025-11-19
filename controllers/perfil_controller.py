from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from PySide6.QtGui import QPixmap

from views.perfil_usuario_ui import VentanaPerfilUsuario


class PerfilUsuarioController(QWidget):
    def __init__(self, app, usuario, user_service, vehiculo_repo):
        super().__init__()

        self.app = app
        self.usuario = usuario
        self.user_service = user_service
        self.vehiculo_repo = vehiculo_repo

        self.ui = VentanaPerfilUsuario()
        self.ui.setupUi(self)

        # ============================
        #   CARGAR DATOS DEL USUARIO
        # ============================
        self.cargar_datos_usuario()

        # ============================
        #   BOTONES
        # ============================
        self.ui.botonVolver.clicked.connect(self.close)
        self.ui.botonEditar.clicked.connect(self.activar_edicion)
        self.ui.botonGuardarCambios.clicked.connect(self.guardar_cambios)
        

        # ============================
        #   ESTADÍSTICAS
        # ============================
      

    # --------------------------------------------
    #   CARGAR DATOS DEL USUARIO
    # --------------------------------------------
    def cargar_datos_usuario(self):
        u = self.usuario

        self.ui.entradaNombre.setText(u.nombre)
        self.ui.entradaApellidos.setText(u.apellidos)
        self.ui.entradaUsername.setText(u.username)
        self.ui.entradaEmail.setText(u.email)
        self.ui.entradaTelefono.setText(u.telefono)
        self.ui.entradaCiudad.setText(u.ciudad)

        # foto perfil (más adelante puedes guardarla en BD)
        try:
            self.ui.labelFoto.setPixmap(
                QPixmap("data/default_user.png").scaled(140, 140)
            )
        except:
            pass

    # --------------------------------------------
    #   ACTIVAR EDICIÓN
    # --------------------------------------------
    def activar_edicion(self):
        self.ui.entradaEmail.setEnabled(True)
        self.ui.entradaTelefono.setEnabled(True)
        self.ui.entradaCiudad.setEnabled(True)

        self.ui.botonGuardarCambios.setEnabled(True)
        self.ui.botonEditar.setEnabled(False)

    # --------------------------------------------
    #   GUARDAR CAMBIOS EN BASE DE DATOS
    # --------------------------------------------
    def guardar_cambios(self):
        nuevo_email = self.ui.entradaEmail.text().strip()
        nuevo_tel = self.ui.entradaTelefono.text().strip()
        nueva_ciudad = self.ui.entradaCiudad.text().strip()

        # VALIDACIÓN EMAIL
        if "@gmail.com" not in nuevo_email and "@hotmail.com" not in nuevo_email and "@outlook.com" not in nuevo_email:
            QMessageBox.warning(self, "Error", "El email no es válido")
            return

        # VALIDACIÓN TELÉFONO
        if not nuevo_tel.isdigit() or len(nuevo_tel) < 9:
            QMessageBox.warning(self, "Error", "El teléfono debe tener al menos 9 números")
            return

        # Actualizar usuario en memoria
        self.usuario.email = nuevo_email
        self.usuario.telefono = nuevo_tel
        self.usuario.ciudad = nueva_ciudad

        # Actualizar base de datos
        self.user_service.actualizar_usuario(self.usuario)

        QMessageBox.information(self, "Correcto", "Datos actualizados correctamente.")

        # Bloquear de nuevo los campos
        self.ui.entradaEmail.setEnabled(False)
        self.ui.entradaTelefono.setEnabled(False)
        self.ui.entradaCiudad.setEnabled(False)

        self.ui.botonGuardarCambios.setEnabled(False)
        self.ui.botonEditar.setEnabled(True)

    #
