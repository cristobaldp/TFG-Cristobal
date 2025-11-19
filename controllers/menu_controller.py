from PySide6.QtWidgets import QMainWindow, QApplication
from views.menu_ui import VentanaMenu
from controllers.vehiculos_controller import VehiculosController


class MenuController(QMainWindow):
    def __init__(self, app, usuario):
        super().__init__()
        self.app = app
        self.usuario = usuario

        self.ui = VentanaMenu()
        self.ui.setupUi(self)

        # ============================
        #   TEXTO DE BIENVENIDA
        # ============================
        self.ui.labelBienvenida.setText(f"Bienvenido, {usuario.nombre}")

        # ============================
        #   EMOJIS EN BOTONES
        # ============================
        self.ui.botonVehiculos.setText("🚗  Gestionar Vehículos")
        self.ui.botonRepostajes.setText("⛽  Repostajes")
        self.ui.botonMapaGasolineras.setText("🗺️  Mapa de Gasolineras")
        self.ui.botonHistorial.setText("📜  Historial")
        self.ui.botonEstadisticas.setText("📊  Estadísticas")
        self.ui.botonPerfil.setText("👤  Perfil del Usuario")
        self.ui.botonAjustes.setText("⚙️  Ajustes")
        self.ui.botonCerrarSesion.setText("🔐  Cerrar Sesión")
        self.ui.botonSalir.setText("❌  Salir")

        # ============================
        #   CONEXIONES
        # ============================
        self.ui.botonVehiculos.clicked.connect(self.abrir_vehiculos)
        self.ui.botonRepostajes.clicked.connect(self.abrir_repostajes)
        self.ui.botonMapaGasolineras.clicked.connect(self.abrir_mapa)
        self.ui.botonHistorial.clicked.connect(self.abrir_historial)
        self.ui.botonEstadisticas.clicked.connect(self.abrir_estadisticas)

        # PERFIL → LLAMA AL APPCONTROLLER
        self.ui.botonPerfil.clicked.connect(self.abrir_perfil)

        # AJUSTES
        self.ui.botonAjustes.clicked.connect(self.abrir_ajustes)

        # SESIÓN
        self.ui.botonCerrarSesion.clicked.connect(self.cerrar_sesion)
        self.ui.botonSalir.clicked.connect(self.salir_app)

    # ========================================
    #              FUNCIONES
    # ========================================

    def abrir_vehiculos(self):
        self.ventanaVehiculos = VehiculosController(
            self.app,
            self.app.vehiculo_service,
            self.app.vehiculo_repo,
            self.usuario
        )
        self.ventanaVehiculos.show()

    def abrir_repostajes(self):
        print("🔧 Repostajes pendiente de implementar")

    def abrir_mapa(self):
        print("🗺️ Mapa pendiente de implementar")

    def abrir_historial(self):
        print("📜 Historial pendiente")

    def abrir_estadisticas(self):
        print("📊 Estadísticas pendientes")

    def abrir_perfil(self):
        """Llama al PerfilUsuarioController desde el AppController."""
        self.app.open_perfil(self.usuario)

    def abrir_ajustes(self):
        """Llama a la ventana Ajustes desde AppController."""
        self.app.open_ajustes(self.usuario)

    def cerrar_sesion(self):
        self.close()
        self.app.show_login()

    def salir_app(self):
        QApplication.quit()
