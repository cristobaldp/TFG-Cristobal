from PySide6.QtWidgets import QApplication

# Controladores
from controllers.login_controller import LoginController
from controllers.registro_controller import RegistroController
from controllers.menu_controller import MenuController

# Base de datos
from data.database import Database

# Repositorios
from repositories.usuario_repository import UsuarioRepository
from repositories.vehiculo_repository import VehiculoRepository

# Servicios
from services.usuario_service import UsuarioService
from services.cities_service import CitiesService
from services.vehiculo_service import VehiculoService


class AppController:
    def __init__(self):
        # ---------------------------
        #   BASE DE DATOS
        # ---------------------------
        self.db = Database()

        # ---------------------------
        #   REPOSITORIOS
        # ---------------------------
        self.user_repo = UsuarioRepository(self.db)
        self.vehiculo_repo = VehiculoRepository(self.db)

        # ---------------------------
        #   SERVICIOS
        # ---------------------------
        self.user_service = UsuarioService(self.user_repo)
        self.cities_service = CitiesService("data/ciudades.txt")
        self.vehiculo_service = VehiculoService("data/marcas_modelos.json")

        # ---------------------------
        #   MOSTRAR LOGIN INICIAL
        # ---------------------------
        self.show_login()

    # ---------------------------
    #   LOGIN
    # ---------------------------
    def show_login(self):
        self.login = LoginController(self, self.user_service)
        self.login.show()

    # ---------------------------
    #   REGISTRO
    # ---------------------------
    def show_registro(self):
        self.registro = RegistroController(self, self.user_service, self.cities_service)
        self.registro.show()

    # ---------------------------
    #   ABRIR MENÚ PRINCIPAL
    # ---------------------------
    def open_menu(self, usuario):
        self.menu = MenuController(self, usuario)
        self.menu.show()

    # ---------------------------
    #   ABRIR GESTION VEHICULOS (WINDOW APARTE)
    # ---------------------------
    def open_vehiculos(self, usuario):
        """
        Esta función se llamaba desde el Menú de Ayer.
        Abría la ventana de 'Gestionar Vehículos' por separado.
        Este comportamiento se mantiene.
        """
        from controllers.vehiculos_controller import VehiculosController

        self.vehiculos = VehiculosController(
            self,
            self.vehiculo_service,
            self.vehiculo_repo,
            usuario
        )
        self.vehiculos.show()
