from PySide6.QtWidgets import QDialog, QMessageBox
from views.vehiculo_anadir_ui import VentanaAnadirVehiculo

class VehiculoAnadirController(QDialog):
    def __init__(self, app, vehiculo_service, vehiculo_repo, usuario):
        super().__init__()
        self.app = app
        self.service = vehiculo_service
        self.repo = vehiculo_repo
        self.usuario = usuario

        self.ui = VentanaAnadirVehiculo()
        self.ui.setupUi(self)

        # Cargar tipos (Coche, Moto…)
        self.ui.comboBoxTipo.clear()
        self.ui.comboBoxTipo.addItems(self.service.obtener_tipos())

        # Conexiones
        self.ui.comboBoxTipo.currentTextChanged.connect(self.cargar_marcas)
        self.ui.comboBoxMarca.currentTextChanged.connect(self.cargar_modelos)
        self.ui.botonGuardar.clicked.connect(self.guardar)
        self.ui.botonVolver.clicked.connect(self.close)

        # Cargar marcas al iniciar por defecto
        self.cargar_marcas()

    def cargar_marcas(self):
        tipo = self.ui.comboBoxTipo.currentText()
        marcas = self.service.obtener_marcas(tipo)
        self.ui.comboBoxMarca.clear()
        self.ui.comboBoxMarca.addItems(marcas)
        self.cargar_modelos()

    def cargar_modelos(self):
        tipo = self.ui.comboBoxTipo.currentText()
        marca = self.ui.comboBoxMarca.currentText()
        modelos = self.service.obtener_modelos(tipo, marca)
        self.ui.comboBoxModelo.clear()
        self.ui.comboBoxModelo.addItems(modelos)

    def guardar(self):
        tipo = self.ui.comboBoxTipo.currentText()
        marca = self.ui.comboBoxMarca.currentText()
        modelo = self.ui.comboBoxModelo.currentText()
        matricula = self.ui.entradaMatricula.text().strip()
        anio = self.ui.entradaAnio.text().strip()
        combustible = self.ui.comboBoxCombustible.currentText()
        consumo = self.ui.entradaConsumo.text().strip()

        # Validar datos
        ok, msg = self.service.validar_vehiculo(matricula, anio, consumo)
        if not ok:
            QMessageBox.warning(self, "Error", msg)
            return

        exito = self.repo.insertar(
            self.usuario.id, tipo, marca, modelo, matricula, anio, combustible, consumo
        )

        if exito:
            QMessageBox.information(self, "Éxito", "Vehículo guardado correctamente")
            self.close()
        else:
            QMessageBox.critical(self, "Error", "No se pudo guardar el vehículo")
