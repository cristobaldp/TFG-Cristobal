import json
import os
from PySide6.QtWidgets import QApplication

# Controladores
from controllers.login_controller import LoginController
from controllers.registro_controller import RegistroController
from controllers.menu_controller import MenuController
from controllers.ajustes_controller import AjustesController
from controllers.vehiculos_controller import VehiculosController

# Base de datos
from data.database import Database

# Repositorios
from repositories.usuario_repository import UsuarioRepository
from repositories.vehiculo_repository import VehiculoRepository

# Servicios
from services.usuario_service import UsuarioService
from services.cities_service import CitiesService
from services.vehiculo_service import VehiculoService

# Estilos
from styles.estilos import ESTILOS


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
        #   CARGAR TEMA GUARDADO
        # ---------------------------
        self.cargar_tema_inicial()

        # ---------------------------
        #   MOSTRAR LOGIN
        # ---------------------------
        self.show_login()

    # ======================================================
    #   ESTILOS
    # ======================================================
    def aplicar_estilo(self, tema):
        estilo = ESTILOS.get(tema, ESTILOS["claro"])

        qss = f"""
        QWidget {{
            background-color: {estilo['background']};
            color: {estilo['text']};
        }}

        QPushButton {{
            background-color: {estilo['button_bg']};
            color: {estilo['text']};
            border: 1px solid {estilo['border']};
            padding: 6px;
            border-radius: 6px;
        }}

        QPushButton:hover {{
            background-color: {estilo['button_hover']};
        }}

        QLineEdit, QComboBox {{
            background-color: {estilo['background']};
            color: {estilo['text']};
            border: 1px solid {estilo['border']};
            padding: 4px;
            border-radius: 4px;
        }}

        /* CHECKBOX FIX */
        QCheckBox::indicator {{
            width: 18px;
            height: 18px;
            border-radius: 4px;
            border: 2px solid {estilo['border']};
            background: {estilo['background']};
        }}

        QCheckBox::indicator:checked {{
            background-color: {estilo['button_hover']};
            image: url(data/check.png);
        }}
        """

        QApplication.instance().setStyleSheet(qss)

    def cargar_tema_inicial(self):
        """Carga el tema desde config.json o usa claro por defecto."""
        ruta = "data/config.json"

        if not os.path.exists(ruta):
            self.aplicar_estilo("claro")
            return

        try:
            with open(ruta, "r", encoding="utf-8") as f:
                datos = json.load(f)
                tema = datos.get("tema", "claro").lower()
        except:
            tema = "claro"

        self.aplicar_estilo(tema)

    # ======================================================
    #   CONTROLADORES DE VENTANAS
    # ======================================================
    def show_login(self):
        self.login = LoginController(self, self.user_service)
        self.login.show()

    def show_registro(self):
        self.registro = RegistroController(self, self.user_service, self.cities_service)
        self.registro.show()

    def open_menu(self, usuario):
        self.menu = MenuController(self, usuario)
        self.menu.show()

    def open_vehiculos(self, usuario):
        """Abre la gestión de vehículos."""
        self.vehiculos = VehiculosController(
            self,
            self.vehiculo_service,
            self.vehiculo_repo,
            usuario
        )
        self.vehiculos.show()

    def open_ajustes(self, usuario):
        self.ajustes = AjustesController(self, usuario)
        self.ajustes.show()
