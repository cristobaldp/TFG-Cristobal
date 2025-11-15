from PySide6.QtWidgets import QMainWindow,QApplication
from views.menu_ui import VentanaMenu
from controllers.vehiculos_controller import VehiculosController



class MenuController(QMainWindow):
    def __init__(self, app, usuario):
        super().__init__()
        self.app = app
        self.usuario = usuario

        self.ui = VentanaMenu()
        self.ui.setupUi(self)

        # Cambiar texto bienvenida
        self.ui.labelBienvenida.setText(f"Bienvenido, {usuario.nombre}")

        # ========= AÑADIR EMOJIS DESDE PYTHON =========
        self.ui.botonVehiculos.setText("🚗  " + self.ui.botonVehiculos.text())
        self.ui.botonRepostajes.setText("⛽  " + self.ui.botonRepostajes.text())
        self.ui.botonMapaGasolineras.setText("🗺️  " + self.ui.botonMapaGasolineras.text())
        self.ui.botonHistorial.setText("📜  " + self.ui.botonHistorial.text())
        self.ui.botonEstadisticas.setText("📊  " + self.ui.botonEstadisticas.text())
        self.ui.botonPerfil.setText("👤  " + self.ui.botonPerfil.text())
        self.ui.botonAjustes.setText("⚙️  " + self.ui.botonAjustes.text())
        self.ui.botonCerrarSesion.setText("🔐  " + self.ui.botonCerrarSesion.text())
        self.ui.botonSalir.setText("❌  " + self.ui.botonSalir.text())
        # ===============================================

        # ========= CONEXIONES =========
        self.ui.botonVehiculos.clicked.connect(self.abrir_vehiculos)
        self.ui.botonRepostajes.clicked.connect(self.abrir_repostajes)
        self.ui.botonMapaGasolineras.clicked.connect(self.abrir_mapa)
        self.ui.botonHistorial.clicked.connect(self.abrir_historial)
        self.ui.botonEstadisticas.clicked.connect(self.abrir_estadisticas)
        self.ui.botonPerfil.clicked.connect(self.abrir_perfil)
        self.ui.botonAjustes.clicked.connect(self.abrir_ajustes)
        self.ui.botonCerrarSesion.clicked.connect(self.cerrar_sesion)
        self.ui.botonSalir.clicked.connect(self.salir_completamente)
        # ===============================================

    # ------------ NAVEGACIÓN ------------

    def abrir_vehiculos(self):
        """Abre la ventana de gestión de vehículos (en otra ventana)."""
        self.ventanaVehiculos = VehiculosController(
            self.app,
            self.app.vehiculo_service,
            self.app.vehiculo_repo,
            self.usuario
        )
        self.ventanaVehiculos.show()

    def abrir_repostajes(self):
        print("Abrir repostajes (no implementado).")

    def abrir_mapa(self):
        print("Mapa de gasolineras (no implementado).")

    def abrir_historial(self):
        print("Abrir historial.")

    def abrir_estadisticas(self):
        print("Abrir estadísticas.")

    def abrir_perfil(self):
        print("Abrir perfil del usuario.")

    def abrir_ajustes(self):
        print("Abrir ajustes.")

    def cerrar_sesion(self):
        self.close()
        self.app.show_login()

    def salir_completamente(self):
        QApplication.quit()
