from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ventanaConsultasFacturas import VentanaConsultasFacturas

import sys
import os
path = os.path.abspath('Controller/')
sys.path.append(path)

import controller_cliente 
import controller_facturas

class Ui_cliente(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(666, 780)
        MainWindow.setStyleSheet("background-color: rgb(232, 237, 240);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 0, 641, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_1 = QtWidgets.QFrame(self.centralwidget)
        self.line_1.setGeometry(QtCore.QRect(0, 10, 20, 701))
        self.line_1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(640, 10, 20, 701))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 710, 641, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(30, 30, 601, 671))
        self.frame_2.setStyleSheet("background-color: rgb(219, 233, 239);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(750, 210, 181, 31))
        self.pushButton.setStyleSheet("background-color: rgb(232, 237, 240);\n"
"font: 9pt \"OCR A Extended\";")
        self.pushButton.setObjectName("pushButton")
        self.textoCedula = QtWidgets.QLineEdit(self.frame_2)
        self.textoCedula.setGeometry(QtCore.QRect(226, 230, 231, 31))
        self.textoCedula.setStyleSheet("background-color: rgb(232, 237, 240);\n"
"font: 9pt \"OCR A Extended\";")
        self.textoCedula.setText("")
        self.textoCedula.setObjectName("textoCedula")
        self.textoNombre = QtWidgets.QLineEdit(self.frame_2)
        self.textoNombre.setGeometry(QtCore.QRect(226, 300, 231, 31))
        self.textoNombre.setStyleSheet("background-color: rgb(232, 237, 240);\n"
"font: 9pt \"OCR A Extended\";")
        self.textoNombre.setText("")
        self.textoNombre.setObjectName("textoNombre")
        self.labelNombre = QtWidgets.QLabel(self.frame_2)
        self.labelNombre.setGeometry(QtCore.QRect(130, 300, 81, 20))
        self.labelNombre.setStyleSheet("font: 10pt \"OCR A Extended\";")
        self.labelNombre.setObjectName("labelNombre")
        self.labelCedula = QtWidgets.QLabel(self.frame_2)
        self.labelCedula.setGeometry(QtCore.QRect(130, 230, 71, 20))
        self.labelCedula.setStyleSheet("font: 10pt \"OCR A Extended\";")
        self.labelCedula.setObjectName("labelCedula")
        self.botonAgregarCliente = QtWidgets.QPushButton(self.frame_2)
        self.botonAgregarCliente.setGeometry(QtCore.QRect(340, 430, 181, 31))
        self.botonAgregarCliente.setStyleSheet("background-color: rgb(232, 237, 240);\n"
"font: 9pt \"OCR A Extended\";")
        self.botonAgregarCliente.setObjectName("botonAgregarCliente")
        self.botonConsultarFacturasCliente = QtWidgets.QPushButton(self.frame_2)
        self.botonConsultarFacturasCliente.setGeometry(QtCore.QRect(90, 430, 181, 31))
        self.botonConsultarFacturasCliente.setStyleSheet("background-color: rgb(232, 237, 240);\n"
"font: 9pt \"OCR A Extended\";")
        self.botonConsultarFacturasCliente.setObjectName("botonConsultarFacturasCliente")
        self.botonEliminarCliente = QtWidgets.QPushButton(self.frame_2)
        self.botonEliminarCliente.setGeometry(QtCore.QRect(220, 500, 181, 31))
        self.botonEliminarCliente.setStyleSheet("background-color: rgb(232, 237, 240);\n"
"font: 9pt \"OCR A Extended\";")
        self.botonEliminarCliente.setObjectName("botonEliminarCliente")
        self.labelCedula_2 = QtWidgets.QLabel(self.frame_2)
        self.labelCedula_2.setGeometry(QtCore.QRect(195, 110, 281, 20))
        self.labelCedula_2.setStyleSheet("font: 12pt \"OCR A Extended\";")
        self.labelCedula_2.setObjectName("labelCedula_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.botonAgregarCliente.clicked.connect(self.validar_campos)
        self.botonConsultarFacturasCliente.clicked.connect(self.consultarFacturasCliente)
        self.botonEliminarCliente.clicked.connect(self.eliminarCliente)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Agregar Propietario"))
        self.labelNombre.setText(_translate("MainWindow", "Nombre:"))
        self.labelCedula.setText(_translate("MainWindow", "Cédula:"))
        self.botonAgregarCliente.setText(_translate("MainWindow", "Agregar Cliente"))
        self.botonEliminarCliente.setText(_translate("MainWindow", "Eliminar Cliente"))
        self.botonConsultarFacturasCliente.setText(_translate("MainWindow", "Ver Facturas"))
        self.labelCedula_2.setText(_translate("MainWindow", "GESTIÓN DE CLIENTES"))

    def validar_campos(self):
        nombre = self.textoNombre.text()
        cedula = self.textoCedula.text()

        if not nombre or not cedula:
            QMessageBox.warning(self, "Campos vacíos", "Por favor, ingrese todos los campos.")
        elif cedula.isdigit():
                datos = {
                        'nombre': nombre,
                        'cedula': cedula
                }
                respuesta = controller_cliente.crear_cliente(datos)

                if respuesta['success']:
                        QMessageBox.information(self, "Operacion exitosa", respuesta['mensaje'])
                else:
                        QMessageBox.warning(self, "Operacion fallida", respuesta['mensaje'])
        else:
                QMessageBox.warning(self, "Error:",'La cédula debe contener solo números')

    def consultarFacturasCliente(self):
        cedula = self.textoCedula.text()
        nombre = self.textoNombre.text()

        if not nombre or not cedula:
                QMessageBox.warning(self, "Campos vacíos", "Por favor, ingrese todos los campos.")
        elif cedula.isdigit():
                datos = {'nombre': nombre,'cedula': cedula}
                verificar_existencia = controller_cliente.buscar_cliente(datos)
                if verificar_existencia['success']:
                        facturas_cliente = controller_cliente.buscar_facturas(verificar_existencia['cliente'])
                        facturas_cliente = controller_facturas.leer_facturas(facturas_cliente['facturas'])
                        ConsultasFacturas = VentanaConsultasFacturas(facturas_cliente)
                        #VentanaConsultasFacturas.consultarFacturas(datos)
                        ConsultasFacturas.exec_()
                else:
                        QMessageBox.warning(self, "Error:", verificar_existencia['mensaje'])
        else:
                QMessageBox.warning(self, "Error:",'La cédula debe contener solo números')

    def eliminarCliente(self):
        nombre = self.textoNombre.text()
        cedula = self.textoCedula.text()

        if not nombre or not cedula:
            QMessageBox.warning(self, "Campos vacíos", "Por favor, ingrese todos los campos.")
        elif cedula.isdigit():
                datos = {'nombre': nombre,'cedula': cedula}
                eliminar = controller_cliente.eliminar_cliente(datos)
                QMessageBox.information(self, "Respuesta:", eliminar['mensaje'])
        else:
                QMessageBox.warning(self, "Error:",'La cédula debe contener solo números')