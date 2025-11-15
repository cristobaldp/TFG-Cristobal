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

        # =======================================================
        # CARGAR TIPOS (ya están en el .ui, pero los refrescamos)
        # =======================================================
        tipos = self.service.obtener_tipos()
        self.ui.comboBoxTipo.clear()
        self.ui.comboBoxTipo.addItems(tipos)

        # =======================================================
        # CARGAR MARCAS/MODELOS
        # =======================================================
        self.ui.comboBoxTipo.currentTextChanged.connect(self.cargar_marcas)
        self.ui.comboBoxMarca.currentTextChanged.connect(self.cargar_modelos)

        # Primera carga
        self.cargar_marcas(self.ui.comboBoxTipo.currentText())

        # =======================================================
        # BOTONES
        # =======================================================
        self.ui.botonGuardar.clicked.connect(self.guardar)
        self.ui.botonVolver.clicked.connect(self.close)

    # =======================================================
    # AL CAMBIAR TIPO → CARGAR MARCAS
    # =======================================================
    def cargar_marcas(self, tipo):
        marcas = self.service.obtener_marcas(tipo)
        self.ui.comboBoxMarca.clear()
        self.ui.comboBoxMarca.addItems(marcas)

        if marcas:
            self.cargar_modelos(marcas[0])

    # =======================================================
    # AL CAMBIAR MARCA → CARGAR MODELOS
    # =======================================================
    def cargar_modelos(self, marca):
        tipo = self.ui.comboBoxTipo.currentText()
        modelos = self.service.obtener_modelos(tipo, marca)
        self.ui.comboBoxModelo.clear()
        self.ui.comboBoxModelo.addItems(modelos)

    # =======================================================
    # GUARDAR VEHÍCULO
    # =======================================================
    def guardar(self):
        tipo = self.ui.comboBoxTipo.currentText()
        marca = self.ui.comboBoxMarca.currentText()
        modelo = self.ui.comboBoxModelo.currentText()
        matricula = self.ui.entradaMatricula.text().strip()
        anio = self.ui.entradaAnio.text().strip()
        combustible = self.ui.comboBoxCombustible.currentText()
        consumo = self.ui.entradaConsumo.text().strip()

        # Validacion
        valido, msg = self.service.validar_vehiculo(matricula, anio, consumo)
        if not valido:
            QMessageBox.warning(self, "Error", msg)
            return

        ok = self.repo.insertar(
            self.usuario.id,
            tipo,
            marca,
            modelo,
            matricula,
            anio,
            combustible,
            float(consumo)
        )

        if ok:
            QMessageBox.information(self, "Correcto", "Vehículo añadido correctamente.")
            self.accept()
        else:
            QMessageBox.critical(self, "Error", "No se pudo añadir el vehículo.")
