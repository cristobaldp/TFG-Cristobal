# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vehiculos.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class VentanaVehiculos(object):
    def setupUi(self, VentanaVehiculos):
        if not VentanaVehiculos.objectName():
            VentanaVehiculos.setObjectName(u"VentanaVehiculos")
        VentanaVehiculos.resize(700, 450)
        self.verticalLayout = QVBoxLayout(VentanaVehiculos)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelTitulo = QLabel(VentanaVehiculos)
        self.labelTitulo.setObjectName(u"labelTitulo")
        self.labelTitulo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelTitulo)

        self.tableVehiculos = QTableWidget(VentanaVehiculos)
        self.tableVehiculos.setObjectName(u"tableVehiculos")

        self.verticalLayout.addWidget(self.tableVehiculos)

        self.horizontalLayoutButtons = QHBoxLayout()
        self.horizontalLayoutButtons.setObjectName(u"horizontalLayoutButtons")
        self.botonAnadir = QPushButton(VentanaVehiculos)
        self.botonAnadir.setObjectName(u"botonAnadir")

        self.horizontalLayoutButtons.addWidget(self.botonAnadir)

        self.botonEditar = QPushButton(VentanaVehiculos)
        self.botonEditar.setObjectName(u"botonEditar")

        self.horizontalLayoutButtons.addWidget(self.botonEditar)

        self.botonEliminar = QPushButton(VentanaVehiculos)
        self.botonEliminar.setObjectName(u"botonEliminar")

        self.horizontalLayoutButtons.addWidget(self.botonEliminar)

        self.botonVolver = QPushButton(VentanaVehiculos)
        self.botonVolver.setObjectName(u"botonVolver")

        self.horizontalLayoutButtons.addWidget(self.botonVolver)


        self.verticalLayout.addLayout(self.horizontalLayoutButtons)


        self.retranslateUi(VentanaVehiculos)

        QMetaObject.connectSlotsByName(VentanaVehiculos)
    # setupUi

    def retranslateUi(self, VentanaVehiculos):
        VentanaVehiculos.setWindowTitle(QCoreApplication.translate("VentanaVehiculos", u"Gesti\u00f3n de Veh\u00edculos", None))
        self.labelTitulo.setText(QCoreApplication.translate("VentanaVehiculos", u"Mis Veh\u00edculos", None))
        self.labelTitulo.setStyleSheet(QCoreApplication.translate("VentanaVehiculos", u"font-size:18px; font-weight:bold;", None))
        self.botonAnadir.setText(QCoreApplication.translate("VentanaVehiculos", u"A\u00f1adir", None))
        self.botonEditar.setText(QCoreApplication.translate("VentanaVehiculos", u"Editar", None))
        self.botonEliminar.setText(QCoreApplication.translate("VentanaVehiculos", u"Eliminar", None))
        self.botonVolver.setText(QCoreApplication.translate("VentanaVehiculos", u"Volver", None))
    # retranslateUi

