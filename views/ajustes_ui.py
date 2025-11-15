# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ajustes.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_VentanaAjustes(object):
    def setupUi(self, VentanaAjustes):
        if not VentanaAjustes.objectName():
            VentanaAjustes.setObjectName(u"VentanaAjustes")
        VentanaAjustes.resize(420, 520)
        self.verticalLayout = QVBoxLayout(VentanaAjustes)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelTitulo = QLabel(VentanaAjustes)
        self.labelTitulo.setObjectName(u"labelTitulo")
        self.labelTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.labelTitulo)

        self.comboTema = QComboBox(VentanaAjustes)
        self.comboTema.addItem("")
        self.comboTema.addItem("")
        self.comboTema.setObjectName(u"comboTema")

        self.verticalLayout.addWidget(self.comboTema)

        self.comboIdioma = QComboBox(VentanaAjustes)
        self.comboIdioma.addItem("")
        self.comboIdioma.addItem("")
        self.comboIdioma.setObjectName(u"comboIdioma")

        self.verticalLayout.addWidget(self.comboIdioma)

        self.comboRadio = QComboBox(VentanaAjustes)
        self.comboRadio.addItem("")
        self.comboRadio.addItem("")
        self.comboRadio.addItem("")
        self.comboRadio.addItem("")
        self.comboRadio.setObjectName(u"comboRadio")

        self.verticalLayout.addWidget(self.comboRadio)

        self.comboVehiculo = QComboBox(VentanaAjustes)
        self.comboVehiculo.setObjectName(u"comboVehiculo")

        self.verticalLayout.addWidget(self.comboVehiculo)

        self.checkNotificaciones = QCheckBox(VentanaAjustes)
        self.checkNotificaciones.setObjectName(u"checkNotificaciones")
        self.checkNotificaciones.setCheckable(True)
        self.checkNotificaciones.setChecked(True)

        self.verticalLayout.addWidget(self.checkNotificaciones)

        self.botonCambiarPassword = QPushButton(VentanaAjustes)
        self.botonCambiarPassword.setObjectName(u"botonCambiarPassword")

        self.verticalLayout.addWidget(self.botonCambiarPassword)

        self.botonExportar = QPushButton(VentanaAjustes)
        self.botonExportar.setObjectName(u"botonExportar")

        self.verticalLayout.addWidget(self.botonExportar)

        self.botonLimpiarCache = QPushButton(VentanaAjustes)
        self.botonLimpiarCache.setObjectName(u"botonLimpiarCache")

        self.verticalLayout.addWidget(self.botonLimpiarCache)

        self.botonVolver = QPushButton(VentanaAjustes)
        self.botonVolver.setObjectName(u"botonVolver")

        self.verticalLayout.addWidget(self.botonVolver)


        self.retranslateUi(VentanaAjustes)

        QMetaObject.connectSlotsByName(VentanaAjustes)
    # setupUi

    def retranslateUi(self, VentanaAjustes):
        VentanaAjustes.setWindowTitle(QCoreApplication.translate("VentanaAjustes", u"Ajustes", None))
        self.labelTitulo.setStyleSheet(QCoreApplication.translate("VentanaAjustes", u"font-size: 18px; font-weight: bold;", None))
        self.labelTitulo.setText(QCoreApplication.translate("VentanaAjustes", u"Ajustes de la aplicaci\u00f3n", None))
        self.comboTema.setItemText(0, QCoreApplication.translate("VentanaAjustes", u"Claro", None))
        self.comboTema.setItemText(1, QCoreApplication.translate("VentanaAjustes", u"Oscuro", None))

        self.comboIdioma.setItemText(0, QCoreApplication.translate("VentanaAjustes", u"Espa\u00f1ol", None))
        self.comboIdioma.setItemText(1, QCoreApplication.translate("VentanaAjustes", u"Ingl\u00e9s", None))

        self.comboRadio.setItemText(0, QCoreApplication.translate("VentanaAjustes", u"2 km", None))
        self.comboRadio.setItemText(1, QCoreApplication.translate("VentanaAjustes", u"5 km", None))
        self.comboRadio.setItemText(2, QCoreApplication.translate("VentanaAjustes", u"10 km", None))
        self.comboRadio.setItemText(3, QCoreApplication.translate("VentanaAjustes", u"20 km", None))

        self.checkNotificaciones.setText(QCoreApplication.translate("VentanaAjustes", u"Activar notificaciones", None))
        self.botonCambiarPassword.setText(QCoreApplication.translate("VentanaAjustes", u"Cambiar contrase\u00f1a", None))
        self.botonExportar.setText(QCoreApplication.translate("VentanaAjustes", u"Exportar datos", None))
        self.botonLimpiarCache.setText(QCoreApplication.translate("VentanaAjustes", u"Limpiar cach\u00e9", None))
        self.botonVolver.setText(QCoreApplication.translate("VentanaAjustes", u"Volver", None))
    # retranslateUi

