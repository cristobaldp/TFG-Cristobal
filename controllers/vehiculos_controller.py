from PySide6.QtWidgets import (
    QWidget,
    QTableWidgetItem,
    QMessageBox,
    QAbstractItemView
)

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

        # ===============================
        #   CONFIGURAR TABLA
        # ===============================
        headers = ["Tipo", "Marca", "Modelo", "Matrícula", "Año", "Combustible", "Consumo"]
        self.ui.tableVehiculos.setColumnCount(len(headers))
        self.ui.tableVehiculos.setHorizontalHeaderLabels(headers)

        # No permitir edición manual
        self.ui.tableVehiculos.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Seleccionar fila completa
        self.ui.tableVehiculos.setSelectionBehavior(QAbstractItemView.SelectRows)

        # ===============================
        #   BOTONES
        # ===============================
        self.ui.botonAnadir.clicked.connect(self.abrir_anadir)
        self.ui.botonEliminar.clicked.connect(self.eliminar)
        self.ui.botonVolver.clicked.connect(self.close)

        # ===============================
        #   CARGAR VEHÍCULOS
        # ===============================
        self.cargar_vehiculos()

    # ===============================
    #   CARGAR VEHÍCULOS BD
    # ===============================
    def cargar_vehiculos(self):
        datos = self.repo.obtener_por_usuario(self.usuario.id)
        self.ui.tableVehiculos.setRowCount(0)

        for row in datos:
            # row → (id, user_id, tipo, marca, modelo, matricula, anio, combustible, consumo)
            id_, _, tipo, marca, modelo, matricula, anio, combustible, consumo = row

            r = self.ui.tableVehiculos.rowCount()
            self.ui.tableVehiculos.insertRow(r)

            self.ui.tableVehiculos.setItem(r, 0, QTableWidgetItem(tipo))
            self.ui.tableVehiculos.setItem(r, 1, QTableWidgetItem(marca))
            self.ui.tableVehiculos.setItem(r, 2, QTableWidgetItem(modelo))
            self.ui.tableVehiculos.setItem(r, 3, QTableWidgetItem(matricula))
            self.ui.tableVehiculos.setItem(r, 4, QTableWidgetItem(str(anio)))
            self.ui.tableVehiculos.setItem(r, 5, QTableWidgetItem(combustible))
            self.ui.tableVehiculos.setItem(r, 6, QTableWidgetItem(str(consumo)))

            # Guardar ID del vehículo en la primera columna (UserRole = 256)
            self.ui.tableVehiculos.item(r, 0).setData(256, id_)

    # ===============================
    #   AÑADIR VEHÍCULO
    # ===============================
    def abrir_anadir(self):
        dialog = VehiculoAnadirController(
            self.app,
            self.service,
            self.repo,
            self.usuario
        )
        dialog.exec()
        self.cargar_vehiculos()  # Recargar tabla al cerrar

    # ===============================
    #   OBTENER ID DE LA FILA
    # ===============================
    def obtener_id_seleccionado(self):
        items = self.ui.tableVehiculos.selectedItems()
        if not items:
            return None

        row = items[0].row()
        return self.ui.tableVehiculos.item(row, 0).data(256)

    # ===============================
    #   ELIMINAR VEHÍCULO
    # ===============================
    def eliminar(self):
        id_vehiculo = self.obtener_id_seleccionado()

        if not id_vehiculo:
            QMessageBox.warning(self, "Aviso", "Selecciona un vehículo para eliminar.")
            return

        confirmar = QMessageBox.question(
            self,
            "Eliminar",
            "¿Seguro que deseas eliminar este vehículo?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirmar == QMessageBox.Yes:
            self.repo.eliminar(id_vehiculo)
            self.cargar_vehiculos()
