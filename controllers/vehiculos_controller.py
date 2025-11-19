from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView
from views.vehiculos_ui import VentanaVehiculos
from controllers.vehiculo_añadir_controller import VehiculoAnadirController


class VehiculosController(QWidget):
    def __init__(self, app, vehiculo_service, vehiculo_repo, usuario):
        super().__init__()
        self.app = app
        self.service = vehiculo_service
        self.repo = vehiculo_repo
        self.usuario = usuario

        self.ui = VentanaVehiculos()
        self.ui.setupUi(self)

        # Configurar tabla
        headers = ["Tipo", "Marca", "Modelo", "Matrícula", "Año", "Combustible", "Consumo"]
        self.ui.tableVehiculos.setColumnCount(len(headers))
        self.ui.tableVehiculos.setHorizontalHeaderLabels(headers)

        self.ui.tableVehiculos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableVehiculos.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Botones
        self.ui.botonAnadir.clicked.connect(self.abrir_anadir)
        self.ui.botonEliminar.clicked.connect(self.eliminar)
        self.ui.botonVolver.clicked.connect(self.close)

        # Cargar datos
        self.cargar_vehiculos()

    # -------------------------
    def cargar_vehiculos(self):
        datos = self.repo.obtener_por_usuario(self.usuario.id)
        self.ui.tableVehiculos.setRowCount(0)

        for fila in datos:
            (id_, _, tipo, marca, modelo, matricula, anio, combustible, consumo) = fila

            row = self.ui.tableVehiculos.rowCount()
            self.ui.tableVehiculos.insertRow(row)

            self.ui.tableVehiculos.setItem(row, 0, QTableWidgetItem(tipo))
            self.ui.tableVehiculos.setItem(row, 1, QTableWidgetItem(marca))
            self.ui.tableVehiculos.setItem(row, 2, QTableWidgetItem(modelo))
            self.ui.tableVehiculos.setItem(row, 3, QTableWidgetItem(matricula))
            self.ui.tableVehiculos.setItem(row, 4, QTableWidgetItem(str(anio)))
            self.ui.tableVehiculos.setItem(row, 5, QTableWidgetItem(combustible))
            self.ui.tableVehiculos.setItem(row, 6, QTableWidgetItem(str(consumo)))

            # Guardar ID oculto
            self.ui.tableVehiculos.item(row, 0).setData(256, id_)

    # -------------------------
    def abrir_anadir(self):
        dialog = VehiculoAnadirController(self.app, self.service, self.repo, self.usuario)
        if dialog.exec():
            self.cargar_vehiculos()

    # -------------------------
    def obtener_id(self):
        items = self.ui.tableVehiculos.selectedItems()
        if not items:
            return None
        row = items[0].row()
        return self.ui.tableVehiculos.item(row, 0).data(256)

    # -------------------------
    def eliminar(self):
        id_vehiculo = self.obtener_id()
        if not id_vehiculo:
            QMessageBox.warning(self, "Aviso", "Selecciona un vehículo.")
            return

        confirmar = QMessageBox.question(self, "Eliminar",
                                         "¿Seguro que deseas eliminarlo?",
                                         QMessageBox.Yes | QMessageBox.No)

        if confirmar == QMessageBox.Yes:
            self.repo.eliminar(id_vehiculo)
            self.cargar_vehiculos()
