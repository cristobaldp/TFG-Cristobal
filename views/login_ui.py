# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class VentanaLogin(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(409, 310)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelUsuario = QLabel(Form)
        self.labelUsuario.setObjectName(u"labelUsuario")

        self.gridLayout.addWidget(self.labelUsuario, 1, 1, 1, 1)

        self.labelClave = QLabel(Form)
        self.labelClave.setObjectName(u"labelClave")

        self.gridLayout.addWidget(self.labelClave, 2, 1, 1, 1)

        self.entradaClave = QLineEdit(Form)
        self.entradaClave.setObjectName(u"entradaClave")

        self.gridLayout.addWidget(self.entradaClave, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 3, 1, 1)

        self.botonRegistrarse = QPushButton(Form)
        self.botonRegistrarse.setObjectName(u"botonRegistrarse")

        self.gridLayout.addWidget(self.botonRegistrarse, 4, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 5, 2, 1, 1)

        self.entradaUsuario = QLineEdit(Form)
        self.entradaUsuario.setObjectName(u"entradaUsuario")

        self.gridLayout.addWidget(self.entradaUsuario, 1, 2, 1, 1)

        self.BotonInicioSesion = QPushButton(Form)
        self.BotonInicioSesion.setObjectName(u"BotonInicioSesion")

        self.gridLayout.addWidget(self.BotonInicioSesion, 3, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 2, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.labelUsuario.setText(QCoreApplication.translate("Form", u"Usuario:", None))
        self.labelClave.setText(QCoreApplication.translate("Form", u"Contrase\u00f1a:", None))
        self.botonRegistrarse.setText(QCoreApplication.translate("Form", u"Registrar Cuenta", None))
        self.BotonInicioSesion.setText(QCoreApplication.translate("Form", u"Iniciar Sesion", None))
    # retranslateUi

