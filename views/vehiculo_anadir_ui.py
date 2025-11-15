# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vehiculo_anadir.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class VentanaAnadirVehiculo(object):
    def setupUi(self, VentanaAnadirVehiculo):
        if not VentanaAnadirVehiculo.objectName():
            VentanaAnadirVehiculo.setObjectName(u"VentanaAnadirVehiculo")
        VentanaAnadirVehiculo.resize(420, 500)
        self.verticalLayout = QVBoxLayout(VentanaAnadirVehiculo)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelTitulo = QLabel(VentanaAnadirVehiculo)
        self.labelTitulo.setObjectName(u"labelTitulo")
        self.labelTitulo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelTitulo)

        self.comboBoxTipo = QComboBox(VentanaAnadirVehiculo)
        self.comboBoxTipo.addItem("")
        self.comboBoxTipo.addItem("")
        self.comboBoxTipo.addItem("")
        self.comboBoxTipo.addItem("")
        self.comboBoxTipo.addItem("")
        self.comboBoxTipo.setObjectName(u"comboBoxTipo")

        self.verticalLayout.addWidget(self.comboBoxTipo)

        self.comboBoxMarca = QComboBox(VentanaAnadirVehiculo)
        self.comboBoxMarca.setObjectName(u"comboBoxMarca")

        self.verticalLayout.addWidget(self.comboBoxMarca)

        self.comboBoxModelo = QComboBox(VentanaAnadirVehiculo)
        self.comboBoxModelo.setObjectName(u"comboBoxModelo")

        self.verticalLayout.addWidget(self.comboBoxModelo)

        self.entradaMatricula = QLineEdit(VentanaAnadirVehiculo)
        self.entradaMatricula.setObjectName(u"entradaMatricula")

        self.verticalLayout.addWidget(self.entradaMatricula)

        self.entradaAnio = QLineEdit(VentanaAnadirVehiculo)
        self.entradaAnio.setObjectName(u"entradaAnio")

        self.verticalLayout.addWidget(self.entradaAnio)

        self.comboBoxCombustible = QComboBox(VentanaAnadirVehiculo)
        self.comboBoxCombustible.addItem("")
        self.comboBoxCombustible.addItem("")
        self.comboBoxCombustible.addItem("")
        self.comboBoxCombustible.addItem("")
        self.comboBoxCombustible.addItem("")
        self.comboBoxCombustible.setObjectName(u"comboBoxCombustible")

        self.verticalLayout.addWidget(self.comboBoxCombustible)

        self.entradaConsumo = QLineEdit(VentanaAnadirVehiculo)
        self.entradaConsumo.setObjectName(u"entradaConsumo")

        self.verticalLayout.addWidget(self.entradaConsumo)

        self.botonGuardar = QPushButton(VentanaAnadirVehiculo)
        self.botonGuardar.setObjectName(u"botonGuardar")
        self.botonGuardar.setMinimumHeight(40)

        self.verticalLayout.addWidget(self.botonGuardar)

        self.botonVolver = QPushButton(VentanaAnadirVehiculo)
        self.botonVolver.setObjectName(u"botonVolver")
        self.botonVolver.setMinimumHeight(40)

        self.verticalLayout.addWidget(self.botonVolver)


        self.retranslateUi(VentanaAnadirVehiculo)

        QMetaObject.connectSlotsByName(VentanaAnadirVehiculo)
    # setupUi

    def retranslateUi(self, VentanaAnadirVehiculo):
        VentanaAnadirVehiculo.setWindowTitle(QCoreApplication.translate("VentanaAnadirVehiculo", u"A\u00f1adir Veh\u00edculo", None))
        self.labelTitulo.setText(QCoreApplication.translate("VentanaAnadirVehiculo", u"A\u00f1adir Veh\u00edculo", None))
        self.labelTitulo.setStyleSheet(QCoreApplication.translate("VentanaAnadirVehiculo", u"font-size: 20px; font-weight: bold;", None))
        self.comboBoxTipo.setItemText(0, QCoreApplication.translate("VentanaAnadirVehiculo", u"Coche", None))
        self.comboBoxTipo.setItemText(1, QCoreApplication.translate("VentanaAnadirVehiculo", u"Moto", None))
        self.comboBoxTipo.setItemText(2, QCoreApplication.translate("VentanaAnadirVehiculo", u"Furgoneta", None))
        self.comboBoxTipo.setItemText(3, QCoreApplication.translate("VentanaAnadirVehiculo", u"Cami\u00f3n", None))
        self.comboBoxTipo.setItemText(4, QCoreApplication.translate("VentanaAnadirVehiculo", u"Industrial", None))

        self.entradaMatricula.setPlaceholderText(QCoreApplication.translate("VentanaAnadirVehiculo", u"Matr\u00edcula (1234-ABC)", None))
        self.entradaAnio.setPlaceholderText(QCoreApplication.translate("VentanaAnadirVehiculo", u"A\u00f1o", None))
        self.comboBoxCombustible.setItemText(0, QCoreApplication.translate("VentanaAnadirVehiculo", u"Gasolina", None))
        self.comboBoxCombustible.setItemText(1, QCoreApplication.translate("VentanaAnadirVehiculo", u"Di\u00e9sel", None))
        self.comboBoxCombustible.setItemText(2, QCoreApplication.translate("VentanaAnadirVehiculo", u"H\u00edbrido", None))
        self.comboBoxCombustible.setItemText(3, QCoreApplication.translate("VentanaAnadirVehiculo", u"El\u00e9ctrico", None))
        self.comboBoxCombustible.setItemText(4, QCoreApplication.translate("VentanaAnadirVehiculo", u"GLP", None))

        self.entradaConsumo.setPlaceholderText(QCoreApplication.translate("VentanaAnadirVehiculo", u"Consumo (L/100km)", None))
        self.botonGuardar.setText(QCoreApplication.translate("VentanaAnadirVehiculo", u"Guardar Veh\u00edculo", None))
        self.botonVolver.setText(QCoreApplication.translate("VentanaAnadirVehiculo", u"Volver", None))
    # retranslateUi

