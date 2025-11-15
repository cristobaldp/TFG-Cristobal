# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class VentanaMenu(object):
    def setupUi(self, VentanaMenu):
        if not VentanaMenu.objectName():
            VentanaMenu.setObjectName(u"VentanaMenu")
        VentanaMenu.resize(450, 520)
        self.centralwidget = QWidget(VentanaMenu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelBienvenida = QLabel(self.centralwidget)
        self.labelBienvenida.setObjectName(u"labelBienvenida")
        self.labelBienvenida.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelBienvenida)

        self.botonVehiculos = QPushButton(self.centralwidget)
        self.botonVehiculos.setObjectName(u"botonVehiculos")
        self.botonVehiculos.setMinimumHeight(40)

        self.verticalLayout.addWidget(self.botonVehiculos)

        self.botonRepostajes = QPushButton(self.centralwidget)
        self.botonRepostajes.setObjectName(u"botonRepostajes")
        self.botonRepostajes.setMinimumHeight(40)

        self.verticalLayout.addWidget(self.botonRepostajes)

        self.botonMapaGasolineras = QPushButton(self.centralwidget)
        self.botonMapaGasolineras.setObjectName(u"botonMapaGasolineras")
        self.botonMapaGasolineras.setMinimumHeight(40)

        self.verticalLayout.addWidget(self.botonMapaGasolineras)

        self.botonHistorial = QPushButton(self.centralwidget)
        self.botonHistorial.setObjectName(u"botonHistorial")
        self.botonHistorial.setMinimumHeight(40)

        self.verticalLayout.addWidget(self.botonHistorial)

        self.botonEstadisticas = QPushButton(self.centralwidget)
        self.botonEstadisticas.setObjectName(u"botonEstadisticas")
        self.botonEstadisticas.setMinimumHeight(40)

        self.verticalLayout.addWidget(self.botonEstadisticas)

        self.botonPerfil = QPushButton(self.centralwidget)
        self.botonPerfil.setObjectName(u"botonPerfil")
        self.botonPerfil.setMinimumHeight(40)

        self.verticalLayout.addWidget(self.botonPerfil)

        self.botonAjustes = QPushButton(self.centralwidget)
        self.botonAjustes.setObjectName(u"botonAjustes")
        self.botonAjustes.setMinimumHeight(40)

        self.verticalLayout.addWidget(self.botonAjustes)

        self.botonCerrarSesion = QPushButton(self.centralwidget)
        self.botonCerrarSesion.setObjectName(u"botonCerrarSesion")
        self.botonCerrarSesion.setMinimumHeight(40)

        self.verticalLayout.addWidget(self.botonCerrarSesion)

        self.botonSalir = QPushButton(self.centralwidget)
        self.botonSalir.setObjectName(u"botonSalir")
        self.botonSalir.setMinimumHeight(40)

        self.verticalLayout.addWidget(self.botonSalir)

        VentanaMenu.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(VentanaMenu)
        self.menubar.setObjectName(u"menubar")
        VentanaMenu.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(VentanaMenu)
        self.statusbar.setObjectName(u"statusbar")
        VentanaMenu.setStatusBar(self.statusbar)

        self.retranslateUi(VentanaMenu)

        QMetaObject.connectSlotsByName(VentanaMenu)
    # setupUi

    def retranslateUi(self, VentanaMenu):
        VentanaMenu.setWindowTitle(QCoreApplication.translate("VentanaMenu", u"Men\u00fa Principal", None))
        self.labelBienvenida.setText(QCoreApplication.translate("VentanaMenu", u"Bienvenido a Kil\u00f3metro a Kil\u00f3metro", None))
        self.labelBienvenida.setStyleSheet(QCoreApplication.translate("VentanaMenu", u"font-size: 18px; font-weight: bold;", None))
        self.botonVehiculos.setText(QCoreApplication.translate("VentanaMenu", u"Gestionar Veh\u00edculos", None))
        self.botonRepostajes.setText(QCoreApplication.translate("VentanaMenu", u"Repostajes", None))
        self.botonMapaGasolineras.setText(QCoreApplication.translate("VentanaMenu", u"Mapa de Gasolineras", None))
        self.botonHistorial.setText(QCoreApplication.translate("VentanaMenu", u"Historial", None))
        self.botonEstadisticas.setText(QCoreApplication.translate("VentanaMenu", u"Estad\u00edsticas", None))
        self.botonPerfil.setText(QCoreApplication.translate("VentanaMenu", u"Perfil del Usuario", None))
        self.botonAjustes.setText(QCoreApplication.translate("VentanaMenu", u"Ajustes", None))
        self.botonCerrarSesion.setText(QCoreApplication.translate("VentanaMenu", u"Cerrar Sesi\u00f3n", None))
        self.botonSalir.setText(QCoreApplication.translate("VentanaMenu", u"Salir", None))
    # retranslateUi

