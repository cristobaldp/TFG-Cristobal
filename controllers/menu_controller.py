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

        # Cambiar texto bienvenida
        self.ui.labelBienvenida.setText(f"Bienvenido, {usuario.nombre}")

        # ========= EMOJIS EN BOTONES =========
        self.ui.botonVehiculos.setText("🚗  " + self.ui.botonVehiculos.text())
        self.ui.botonRepostajes.setText("⛽  " + self.ui.botonRepostajes.text())
        self.ui.botonMapaGasolineras.setText("🗺️  " + self.ui.botonMapaGasolineras.text())
        self.ui.botonHistorial.setText("📜  " + self.ui.botonHistorial.text())
        self.ui.botonEstadisticas.setText("📊  " + self.ui.botonEstadisticas.text())
        self.ui.botonPerfil.setText("👤  " + self.ui.botonPerfil.text())
        self.ui.botonAjustes.setText("⚙️  " + self.ui.botonAjustes.text())
        self.ui.botonCerrarSesion.setText("🔐  " + self.ui.botonCerrarSesion.text())
        self.ui.botonSalir.setText("❌  " + self.ui.botonSalir.text())
        # =====================================

        # ========= CONEXIONES =========
        self.ui.botonVehiculos.clicked.connect(self.abrir_vehiculos)
        self.ui.botonRepostajes.clicked.connect(self.abrir_repostajes)
        self.ui.botonMapaGasolineras.clicked.connect(self.abrir_mapa)
        self.ui.botonHistorial.clicked.connect(self.abrir_historial)
        self.ui.botonEstadisticas.clicked.connect(self.abrir_estadisticas)
        self.ui.botonPerfil.clicked.connect(self.abrir_perfil)

        # AJUSTES (NUEVO) ⭐⭐⭐
        self.ui.botonAjustes.clicked.connect(self.abrir_ajustes)

        self.ui.botonCerrarSesion.clicked.connect(self.cerrar_sesion)
        self.ui.botonSalir.clicked.connect(self.salir_app)
        # ======================================

    # -------- ABRIR GESTIÓN DE VEHÍCULOS --------
    def abrir_vehiculos(self):
        self.ventanaVehiculos = VehiculosController(
            self.app,
            self.app.vehiculo_service,
            self.app.vehiculo_repo,
            self.usuario
        )
        self.ventanaVehiculos.show()

    def abrir_repostajes(self):
        print("Repostajes... (por implementar)")

    def abrir_mapa(self):
        print("Mapa de gasolineras... (por implementar)")

    def abrir_historial(self):
        print("Historial...")

    def abrir_estadisticas(self):
        print("Estadísticas...")

    def abrir_perfil(self):
        print("Perfil del usuario...")

    # -------- ABRIR AJUSTES (NUEVO) -------- ⭐⭐⭐
    def abrir_ajustes(self):
        self.app.open_ajustes(self.usuario)

    # -------- CERRAR SESIÓN --------
    def cerrar_sesion(self):
        self.close()
        self.app.show_login()

    # -------- SALIR COMPLETAMENTE --------
    def salir_app(self):
        QApplication.quit()
