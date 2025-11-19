# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'perfil_usuario.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class VentanaPerfilUsuario(object):
    def setupUi(self, VentanaPerfilUsuario):
        if not VentanaPerfilUsuario.objectName():
            VentanaPerfilUsuario.setObjectName(u"VentanaPerfilUsuario")
        VentanaPerfilUsuario.resize(450, 650)
        self.verticalLayout = QVBoxLayout(VentanaPerfilUsuario)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelFoto = QLabel(VentanaPerfilUsuario)
        self.labelFoto.setObjectName(u"labelFoto")
        self.labelFoto.setMinimumSize(QSize(140, 140))
        self.labelFoto.setMaximumSize(QSize(140, 140))
        self.labelFoto.setAlignment(Qt.AlignCenter)
        self.labelFoto.setStyleSheet(u"\n"
"       border-radius: 70px;\n"
"       background-color: #cfcfcf;\n"
"      ")

        self.verticalLayout.addWidget(self.labelFoto)

        self.botonCambiarFoto = QPushButton(VentanaPerfilUsuario)
        self.botonCambiarFoto.setObjectName(u"botonCambiarFoto")

        self.verticalLayout.addWidget(self.botonCambiarFoto)

        self.labelTituloDatos = QLabel(VentanaPerfilUsuario)
        self.labelTituloDatos.setObjectName(u"labelTituloDatos")
        self.labelTituloDatos.setAlignment(Qt.AlignCenter)
        self.labelTituloDatos.setStyleSheet(u"font-size: 18px; font-weight: bold;")

        self.verticalLayout.addWidget(self.labelTituloDatos)

        self.entradaNombre = QLineEdit(VentanaPerfilUsuario)
        self.entradaNombre.setObjectName(u"entradaNombre")
        self.entradaNombre.setEnabled(False)

        self.verticalLayout.addWidget(self.entradaNombre)

        self.entradaApellidos = QLineEdit(VentanaPerfilUsuario)
        self.entradaApellidos.setObjectName(u"entradaApellidos")
        self.entradaApellidos.setEnabled(False)

        self.verticalLayout.addWidget(self.entradaApellidos)

        self.entradaUsername = QLineEdit(VentanaPerfilUsuario)
        self.entradaUsername.setObjectName(u"entradaUsername")
        self.entradaUsername.setEnabled(False)

        self.verticalLayout.addWidget(self.entradaUsername)

        self.entradaEmail = QLineEdit(VentanaPerfilUsuario)
        self.entradaEmail.setObjectName(u"entradaEmail")
        self.entradaEmail.setEnabled(False)

        self.verticalLayout.addWidget(self.entradaEmail)

        self.entradaTelefono = QLineEdit(VentanaPerfilUsuario)
        self.entradaTelefono.setObjectName(u"entradaTelefono")
        self.entradaTelefono.setEnabled(False)

        self.verticalLayout.addWidget(self.entradaTelefono)

        self.entradaCiudad = QLineEdit(VentanaPerfilUsuario)
        self.entradaCiudad.setObjectName(u"entradaCiudad")
        self.entradaCiudad.setEnabled(False)

        self.verticalLayout.addWidget(self.entradaCiudad)

        self.botonEditar = QPushButton(VentanaPerfilUsuario)
        self.botonEditar.setObjectName(u"botonEditar")

        self.verticalLayout.addWidget(self.botonEditar)

        self.botonGuardarCambios = QPushButton(VentanaPerfilUsuario)
        self.botonGuardarCambios.setObjectName(u"botonGuardarCambios")
        self.botonGuardarCambios.setEnabled(False)

        self.verticalLayout.addWidget(self.botonGuardarCambios)

        self.botonCambiarPassword = QPushButton(VentanaPerfilUsuario)
        self.botonCambiarPassword.setObjectName(u"botonCambiarPassword")

        self.verticalLayout.addWidget(self.botonCambiarPassword)

        self.labelTituloStats = QLabel(VentanaPerfilUsuario)
        self.labelTituloStats.setObjectName(u"labelTituloStats")
        self.labelTituloStats.setAlignment(Qt.AlignCenter)
        self.labelTituloStats.setStyleSheet(u"font-size: 18px; font-weight: bold;")

        self.verticalLayout.addWidget(self.labelTituloStats)

        self.labelStatsVehiculos = QLabel(VentanaPerfilUsuario)
        self.labelStatsVehiculos.setObjectName(u"labelStatsVehiculos")

        self.verticalLayout.addWidget(self.labelStatsVehiculos)

        self.labelStatsRepostajes = QLabel(VentanaPerfilUsuario)
        self.labelStatsRepostajes.setObjectName(u"labelStatsRepostajes")

        self.verticalLayout.addWidget(self.labelStatsRepostajes)

        self.labelStatsGasto = QLabel(VentanaPerfilUsuario)
        self.labelStatsGasto.setObjectName(u"labelStatsGasto")

        self.verticalLayout.addWidget(self.labelStatsGasto)

        self.botonEliminarCuenta = QPushButton(VentanaPerfilUsuario)
        self.botonEliminarCuenta.setObjectName(u"botonEliminarCuenta")
        self.botonEliminarCuenta.setStyleSheet(u"color: red;")

        self.verticalLayout.addWidget(self.botonEliminarCuenta)

        self.botonVolver = QPushButton(VentanaPerfilUsuario)
        self.botonVolver.setObjectName(u"botonVolver")

        self.verticalLayout.addWidget(self.botonVolver)


        self.retranslateUi(VentanaPerfilUsuario)

        QMetaObject.connectSlotsByName(VentanaPerfilUsuario)
    # setupUi

    def retranslateUi(self, VentanaPerfilUsuario):
        VentanaPerfilUsuario.setWindowTitle(QCoreApplication.translate("VentanaPerfilUsuario", u"Perfil del Usuario", None))
        self.labelFoto.setText(QCoreApplication.translate("VentanaPerfilUsuario", u"Foto", None))
        self.botonCambiarFoto.setText(QCoreApplication.translate("VentanaPerfilUsuario", u"Cambiar foto", None))
        self.labelTituloDatos.setText(QCoreApplication.translate("VentanaPerfilUsuario", u"Datos del usuario", None))
        self.entradaNombre.setPlaceholderText(QCoreApplication.translate("VentanaPerfilUsuario", u"Nombre", None))
        self.entradaApellidos.setPlaceholderText(QCoreApplication.translate("VentanaPerfilUsuario", u"Apellidos", None))
        self.entradaUsername.setPlaceholderText(QCoreApplication.translate("VentanaPerfilUsuario", u"Nombre de usuario", None))
        self.entradaEmail.setPlaceholderText(QCoreApplication.translate("VentanaPerfilUsuario", u"Email", None))
        self.entradaTelefono.setPlaceholderText(QCoreApplication.translate("VentanaPerfilUsuario", u"Tel\u00e9fono", None))
        self.entradaCiudad.setPlaceholderText(QCoreApplication.translate("VentanaPerfilUsuario", u"Ciudad", None))
        self.botonEditar.setText(QCoreApplication.translate("VentanaPerfilUsuario", u"Editar perfil", None))
        self.botonGuardarCambios.setText(QCoreApplication.translate("VentanaPerfilUsuario", u"Guardar cambios", None))
        self.botonCambiarPassword.setText(QCoreApplication.translate("VentanaPerfilUsuario", u"Cambiar contrase\u00f1a", None))
        self.labelTituloStats.setText(QCoreApplication.translate("VentanaPerfilUsuario", u"Actividad del usuario", None))
        self.labelStatsVehiculos.setText(QCoreApplication.translate("VentanaPerfilUsuario", u"Veh\u00edculos registrados: 0", None))
        self.labelStatsRepostajes.setText(QCoreApplication.translate("VentanaPerfilUsuario", u"Repostajes realizados: 0", None))
        self.labelStatsGasto.setText(QCoreApplication.translate("VentanaPerfilUsuario", u"Gasto total: 0 \u20ac", None))
        self.botonEliminarCuenta.setText(QCoreApplication.translate("VentanaPerfilUsuario", u"Eliminar cuenta", None))
        self.botonVolver.setText(QCoreApplication.translate("VentanaPerfilUsuario", u"Volver", None))
    # retranslateUi

