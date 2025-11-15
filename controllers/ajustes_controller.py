import json
import os
from PySide6.QtWidgets import QDialog, QMessageBox
from views.ajustes_ui import VentanaAjustes


class AjustesController(QDialog):
    def __init__(self, app, usuario):
        super().__init__()
        self.app = app
        self.usuario = usuario

        self.ui = VentanaAjustes()
        self.ui.setupUi(self)

        self.config_path = "data/config.json"

        # Eliminar estado triestadio (evita el cuadrado raro)
        self.ui.checkNotificaciones.setTristate(False)

        # Cargar configuración + vehículos
        self.cargar_config()
        self.cargar_vehiculos_usuario()

        # Eventos
        self.ui.botonVolver.clicked.connect(self.close)
        self.ui.botonCambiarPassword.clicked.connect(self.cambiar_password)
        self.ui.botonExportar.clicked.connect(self.exportar_csv)
        self.ui.botonLimpiarCache.clicked.connect(self.limpiar_cache)
        self.ui.comboTema.currentTextChanged.connect(self.cambiar_tema)
        self.ui.comboIdioma.currentTextChanged.connect(self.guardar_config)
        self.ui.comboRadio.currentTextChanged.connect(self.guardar_config)
        self.ui.comboVehiculo.currentTextChanged.connect(self.guardar_config)
        self.ui.checkNotificaciones.stateChanged.connect(self.guardar_config)

    # ======================================================
    #   Cargar desde config.json
    # ======================================================
    def cargar_config(self):
        if not os.path.exists(self.config_path):
            return

        with open(self.config_path, "r", encoding="utf-8") as f:
            config = json.load(f)

        # Tema
        tema = config.get("tema", "Claro").capitalize()
        index = self.ui.comboTema.findText(tema)
        if index != -1:
            self.ui.comboTema.setCurrentIndex(index)

        # Idioma
        idioma = config.get("idioma", "Español")
        index = self.ui.comboIdioma.findText(idioma)
        if index != -1:
            self.ui.comboIdioma.setCurrentIndex(index)

        # Radio
        radio = config.get("radio", "5 km")
        index = self.ui.comboRadio.findText(radio)
        if index != -1:
            self.ui.comboRadio.setCurrentIndex(index)

        # Notificaciones
        self.ui.checkNotificaciones.setChecked(config.get("notificaciones", False))

        # Vehículo por defecto se cargará después

    # ======================================================
    #   Guardar JSON
    # ======================================================
    def guardar_config(self):
        config = {
            "tema": self.ui.comboTema.currentText(),
            "idioma": self.ui.comboIdioma.currentText(),
            "radio": self.ui.comboRadio.currentText(),
            "notificaciones": self.ui.checkNotificaciones.isChecked(),
            "vehiculo_defecto": self.ui.comboVehiculo.currentText()
        }

        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)

    # ======================================================
    #   Cambiar tema en tiempo real
    # ======================================================
    def cambiar_tema(self):
        tema = self.ui.comboTema.currentText().lower()
        self.app.aplicar_estilo(tema)
        self.guardar_config()  # Guardar cambio

    # ======================================================
    #   Cargar vehículos del usuario
    # ======================================================
    def cargar_vehiculos_usuario(self):
        vehiculos = self.app.vehiculo_repo.obtener_por_usuario(self.usuario.id)

        self.ui.comboVehiculo.clear()

        if not vehiculos:
            self.ui.comboVehiculo.addItem("Sin vehículos")
            return

        lista_textos = []
        for v in vehiculos:
            # v = (id, user_id, tipo, marca, modelo, matricula, anio, combustible, consumo)
            texto = f"{v[3]} {v[4]} - {v[5]}"
            lista_textos.append(texto)
            self.ui.comboVehiculo.addItem(texto)

        # Seleccionar vehículo guardado
        if os.path.exists(self.config_path):
            with open(self.config_path, "r", encoding="utf-8") as f:
                config = json.load(f)

            veh_def = config.get("vehiculo_defecto", "")
            index = self.ui.comboVehiculo.findText(veh_def)
            if index != -1:
                self.ui.comboVehiculo.setCurrentIndex(index)

    # ======================================================
    #   Implementaciones varias
    # ======================================================
    def exportar_csv(self):
        QMessageBox.information(self, "Exportar CSV", "Aquí exportarás datos reales (pronto).")

    def limpiar_cache(self):
        QMessageBox.information(self, "Limpiar caché", "Caché limpiada correctamente.")

    def cambiar_password(self):
        QMessageBox.information(self, "Cambiar contraseña", "Aquí abrirás un menú para cambiar contraseña.")
