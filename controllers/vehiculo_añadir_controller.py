from PySide6.QtWidgets import QDialog, QMessageBox
from views.vehiculo_anadir_ui import VentanaAnadirVehiculo
import re


class VehiculoAnadirController(QDialog):
    def __init__(self, app, vehiculo_service, vehiculo_repo, usuario):
        super().__init__()
        self.app = app
        self.service = vehiculo_service
        self.repo = vehiculo_repo
        self.usuario = usuario

        self.ui = VentanaAnadirVehiculo()
        self.ui.setupUi(self)

        # --------------------------------------
        #   CARGAR TIPOS DESDE EL JSON
        # --------------------------------------
        self.ui.comboBoxTipo.clear()
        self.ui.comboBoxTipo.addItems(self.service.obtener_tipos())

        # --------------------------------------
        #   CONEXIONES
        # --------------------------------------
        self.ui.comboBoxTipo.currentTextChanged.connect(self.cargar_marcas)
        self.ui.comboBoxMarca.currentTextChanged.connect(self.cargar_modelos)
        self.ui.entradaMatricula.textChanged.connect(self.forzar_mayusculas)

        self.ui.botonGuardar.clicked.connect(self.guardar)
        self.ui.botonVolver.clicked.connect(self.close)

        # --------------------------------------
        #   CARGA INICIAL (SOLUCIÓN A TU PROBLEMA)
        # --------------------------------------
        self.cargar_marcas()   # Esto carga las marcas de "Coche" al iniciar
        self.cargar_modelos()  # Cargar modelos iniciales


    # =====================================================
    # CARGAR MARCAS SEGÚN TIPO
    # =====================================================
    def cargar_marcas(self):
        tipo = self.ui.comboBoxTipo.currentText()
        marcas = self.service.obtener_marcas(tipo)

        self.ui.comboBoxMarca.clear()
        self.ui.comboBoxMarca.addItems(marcas)

        # Cargar modelos de la primera marca disponible
        self.cargar_modelos()


    # =====================================================
    # CARGAR MODELOS SEGÚN MARCA
    # =====================================================
    def cargar_modelos(self):
        tipo = self.ui.comboBoxTipo.currentText()
        marca = self.ui.comboBoxMarca.currentText()

        modelos = self.service.obtener_modelos(tipo, marca)

        self.ui.comboBoxModelo.clear()
        self.ui.comboBoxModelo.addItems(modelos)


    # =====================================================
    # FORZAR MATRÍCULA A MAYÚSCULAS
    # =====================================================
    def forzar_mayusculas(self):
        texto = self.ui.entradaMatricula.text().upper()
        self.ui.entradaMatricula.setText(texto)


    # =====================================================
    # VALIDACIÓN MATRÍCULA (FORMATO REAL 1234-ABC)
    # =====================================================
    def validar_matricula(self, matricula):
        patron = r"^[0-9]{4}-[A-Z]{3}$"
        return re.match(patron, matricula) is not None


    # =====================================================
    # GUARDAR VEHÍCULO EN BD
    # =====================================================
    def guardar(self):
        tipo = self.ui.comboBoxTipo.currentText()
        marca = self.ui.comboBoxMarca.currentText()
        modelo = self.ui.comboBoxModelo.currentText()
        matricula = self.ui.entradaMatricula.text().upper()
        anio = self.ui.entradaAnio.text()
        combustible = self.ui.comboBoxCombustible.currentText()
        consumo = self.ui.entradaConsumo.text()

        # ------------------------
        # Validar matrícula real
        # ------------------------
        if not self.validar_matricula(matricula):
            QMessageBox.warning(self, "Error", "La matrícula debe ser del tipo 1234-ABC")
            return

        # ------------------------
        # Validación adicional del servicio
        # ------------------------
        valido, msg = self.service.validar_vehiculo(matricula, anio, consumo)
        if not valido:
            QMessageBox.warning(self, "Error", msg)
            return

        # ------------------------
        # INSERTAR EN LA BASE DE DATOS
        # ------------------------
        ok = self.repo.insertar(
            self.usuario.id,
            tipo, marca, modelo, matricula, anio, combustible, consumo
        )

        if ok:
            QMessageBox.information(self, "OK", "Vehículo añadido correctamente.")
            self.accept()
        else:
            QMessageBox.critical(self, "Error", "No se pudo guardar el vehículo.")
