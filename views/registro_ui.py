# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registro.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class VentanaRegistro(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(426, 389)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelTelefono = QLabel(Form)
        self.labelTelefono.setObjectName(u"labelTelefono")

        self.gridLayout.addWidget(self.labelTelefono, 16, 1, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 7, 1, 1, 1)

        self.dateEditEdad = QDateEdit(Form)
        self.dateEditEdad.setObjectName(u"dateEditEdad")
        self.dateEditEdad.setCalendarPopup(True)

        self.gridLayout.addWidget(self.dateEditEdad, 9, 3, 1, 1)

        self.botonCrearCuenta = QPushButton(Form)
        self.botonCrearCuenta.setObjectName(u"botonCrearCuenta")

        self.gridLayout.addWidget(self.botonCrearCuenta, 18, 1, 1, 1)

        self.entradaTelefono = QLineEdit(Form)
        self.entradaTelefono.setObjectName(u"entradaTelefono")

        self.gridLayout.addWidget(self.entradaTelefono, 16, 3, 1, 1)

        self.labelClaveRegistro = QLabel(Form)
        self.labelClaveRegistro.setObjectName(u"labelClaveRegistro")

        self.gridLayout.addWidget(self.labelClaveRegistro, 11, 1, 1, 1)

        self.entradaClaveRegistro = QLineEdit(Form)
        self.entradaClaveRegistro.setObjectName(u"entradaClaveRegistro")

        self.gridLayout.addWidget(self.entradaClaveRegistro, 11, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 9, 0, 1, 1)

        self.labelConfirmarClave = QLabel(Form)
        self.labelConfirmarClave.setObjectName(u"labelConfirmarClave")

        self.gridLayout.addWidget(self.labelConfirmarClave, 12, 1, 1, 1)

        self.entradaConfirmarClave = QLineEdit(Form)
        self.entradaConfirmarClave.setObjectName(u"entradaConfirmarClave")

        self.gridLayout.addWidget(self.entradaConfirmarClave, 12, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 19, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 2, 0, 1, 1)

        self.labelEdad = QLabel(Form)
        self.labelEdad.setObjectName(u"labelEdad")

        self.gridLayout.addWidget(self.labelEdad, 9, 1, 1, 1)

        self.botonVolver = QPushButton(Form)
        self.botonVolver.setObjectName(u"botonVolver")

        self.gridLayout.addWidget(self.botonVolver, 0, 0, 1, 1)

        self.entradaApellidos = QLineEdit(Form)
        self.entradaApellidos.setObjectName(u"entradaApellidos")

        self.gridLayout.addWidget(self.entradaApellidos, 7, 3, 1, 1)

        self.labelLocalidad = QLabel(Form)
        self.labelLocalidad.setObjectName(u"labelLocalidad")

        self.gridLayout.addWidget(self.labelLocalidad, 8, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 9, 4, 1, 1)

        self.labelCorreo = QLabel(Form)
        self.labelCorreo.setObjectName(u"labelCorreo")

        self.gridLayout.addWidget(self.labelCorreo, 14, 1, 1, 1)

        self.entradaCorreo = QLineEdit(Form)
        self.entradaCorreo.setObjectName(u"entradaCorreo")

        self.gridLayout.addWidget(self.entradaCorreo, 14, 3, 1, 1)

        self.comboBoxLocalidad = QComboBox(Form)
        self.comboBoxLocalidad.setObjectName(u"comboBoxLocalidad")

        self.gridLayout.addWidget(self.comboBoxLocalidad, 8, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 3, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 1, 0, 1, 1)

        self.entradaNombre = QLineEdit(Form)
        self.entradaNombre.setObjectName(u"entradaNombre")

        self.gridLayout.addWidget(self.entradaNombre, 4, 3, 1, 1)

        self.labelNombre = QLabel(Form)
        self.labelNombre.setObjectName(u"labelNombre")

        self.gridLayout.addWidget(self.labelNombre, 4, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.labelNombreUsuario = QLabel(Form)
        self.labelNombreUsuario.setObjectName(u"labelNombreUsuario")

        self.gridLayout.addWidget(self.labelNombreUsuario, 10, 1, 1, 1)

        self.entradaNombreUsuario = QLineEdit(Form)
        self.entradaNombreUsuario.setObjectName(u"entradaNombreUsuario")

        self.gridLayout.addWidget(self.entradaNombreUsuario, 10, 3, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.labelTelefono.setText(QCoreApplication.translate("Form", u"N\u00ba Telefono", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Apellidos", None))
        self.botonCrearCuenta.setText(QCoreApplication.translate("Form", u"Crear Cuenta", None))
        self.labelClaveRegistro.setText(QCoreApplication.translate("Form", u"Contrase\u00f1a", None))
        self.labelConfirmarClave.setText(QCoreApplication.translate("Form", u"Confirmar Contrase\u00f1a", None))
        self.labelEdad.setText(QCoreApplication.translate("Form", u"Edad", None))
        self.botonVolver.setText(QCoreApplication.translate("Form", u"Volver", None))
        self.labelLocalidad.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Localidad</p></body></html>", None))
        self.labelCorreo.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Correo Electronico</p></body></html>", None))
        self.labelNombre.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Nombre:</p></body></html>", None))
        self.labelNombreUsuario.setText(QCoreApplication.translate("Form", u"Nombre Usuario", None))
    # retranslateUi

