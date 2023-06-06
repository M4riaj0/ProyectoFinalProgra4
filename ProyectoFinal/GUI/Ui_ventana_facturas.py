from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

import sys
import os
path = os.path.abspath('Controller/')
sys.path.append(path)

import controller_cliente 
import controller_facturas 

class Ui_facturas(object):
    listProductos = []

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
        self.textoCedula.setGeometry(QtCore.QRect(290, 80, 231, 31))
        self.textoCedula.setStyleSheet("background-color: rgb(232, 237, 240);\n"
"font: 9pt \"OCR A Extended\";")
        self.textoCedula.setText("")
        self.textoCedula.setObjectName("textoCedula")
        self.labelCedula = QtWidgets.QLabel(self.frame_2)
        self.labelCedula.setGeometry(QtCore.QRect(80, 80, 151, 20))
        self.labelCedula.setStyleSheet("font: 10pt \"OCR A Extended\";")
        self.labelCedula.setObjectName("labelCedula")
        self.botonAgregarFactura = QtWidgets.QPushButton(self.frame_2)
        self.botonAgregarFactura.setGeometry(QtCore.QRect(360, 600, 181, 31))
        self.botonAgregarFactura.setStyleSheet("background-color: rgb(232, 237, 240);\n"
"font: 9pt \"OCR A Extended\";")
        self.botonAgregarFactura.setObjectName("botonAgregarFactura")
        self.labelTitulo = QtWidgets.QLabel(self.frame_2)
        self.labelTitulo.setGeometry(QtCore.QRect(180, 20, 241, 20))
        self.labelTitulo.setStyleSheet("font: 10pt \"OCR A Extended\";")
        self.labelTitulo.setObjectName("labelTitulo")
        self.labelProductosDisponibles = QtWidgets.QLabel(self.frame_2)
        self.labelProductosDisponibles.setGeometry(QtCore.QRect(30, 150, 231, 20))
        self.labelProductosDisponibles.setStyleSheet("font: 10pt \"OCR A Extended\";")
        self.labelProductosDisponibles.setObjectName("labelProductosDisponibles")
        self.checkBoxTrompa = QtWidgets.QCheckBox(self.frame_2)
        self.checkBoxTrompa.setGeometry(QtCore.QRect(80, 240, 181, 20))
        self.checkBoxTrompa.setStyleSheet("font: 8pt \"OCR A Extended\";")
        self.checkBoxTrompa.setObjectName("checkBoxTrompa")
        self.checkBoxRidomil = QtWidgets.QCheckBox(self.frame_2)
        self.checkBoxRidomil.setGeometry(QtCore.QRect(80, 270, 171, 20))
        self.checkBoxRidomil.setStyleSheet("font: 8pt \"OCR A Extended\";")
        self.checkBoxRidomil.setObjectName("checkBoxRidomil")
        self.checkBoxFullneem = QtWidgets.QCheckBox(self.frame_2)
        self.checkBoxFullneem.setGeometry(QtCore.QRect(80, 300, 171, 20))
        self.checkBoxFullneem.setStyleSheet("font: 8pt \"OCR A Extended\";")
        self.checkBoxFullneem.setObjectName("checkBoxFullneem")
        self.labelControlPlagas = QtWidgets.QLabel(self.frame_2)
        self.labelControlPlagas.setGeometry(QtCore.QRect(60, 200, 171, 20))
        self.labelControlPlagas.setStyleSheet("font: 9pt \"OCR A Extended\";")
        self.labelControlPlagas.setObjectName("labelControlPlagas")
        self.checkBoxFosforita = QtWidgets.QCheckBox(self.frame_2)
        self.checkBoxFosforita.setGeometry(QtCore.QRect(340, 300, 171, 20))
        self.checkBoxFosforita.setStyleSheet("font: 8pt \"OCR A Extended\";")
        self.checkBoxFosforita.setObjectName("checkBoxFosforita")
        self.labelControlPlagas_2 = QtWidgets.QLabel(self.frame_2)
        self.labelControlPlagas_2.setGeometry(QtCore.QRect(320, 200, 201, 20))
        self.labelControlPlagas_2.setStyleSheet("font: 9pt \"OCR A Extended\";")
        self.labelControlPlagas_2.setObjectName("labelControlPlagas_2")
        self.checkBoxAbimgra = QtWidgets.QCheckBox(self.frame_2)
        self.checkBoxAbimgra.setGeometry(QtCore.QRect(340, 240, 191, 20))
        self.checkBoxAbimgra.setStyleSheet("font: 8pt \"OCR A Extended\";")
        self.checkBoxAbimgra.setObjectName("checkBoxAbimgra")
        self.checkBoxUrea = QtWidgets.QCheckBox(self.frame_2)
        self.checkBoxUrea.setGeometry(QtCore.QRect(340, 270, 171, 20))
        self.checkBoxUrea.setStyleSheet("font: 8pt \"OCR A Extended\";")
        self.checkBoxUrea.setObjectName("checkBoxUrea")
        self.checkBoxRostum = QtWidgets.QCheckBox(self.frame_2)
        self.checkBoxRostum.setGeometry(QtCore.QRect(210, 460, 111, 20))
        self.checkBoxRostum.setStyleSheet("font: 8pt \"OCR A Extended\";")
        self.checkBoxRostum.setObjectName("checkBoxRostum")
        self.labelControlPlagas_3 = QtWidgets.QLabel(self.frame_2)
        self.labelControlPlagas_3.setGeometry(QtCore.QRect(190, 360, 171, 20))
        self.labelControlPlagas_3.setStyleSheet("font: 9pt \"OCR A Extended\";")
        self.labelControlPlagas_3.setObjectName("labelControlPlagas_3")
        self.checkBoxBenzatinica = QtWidgets.QCheckBox(self.frame_2)
        self.checkBoxBenzatinica.setGeometry(QtCore.QRect(210, 400, 121, 20))
        self.checkBoxBenzatinica.setStyleSheet("font: 8pt \"OCR A Extended\";")
        self.checkBoxBenzatinica.setObjectName("checkBoxBenzatinica")
        self.checkBoxDarxxin = QtWidgets.QCheckBox(self.frame_2)
        self.checkBoxDarxxin.setGeometry(QtCore.QRect(210, 430, 111, 20))
        self.checkBoxDarxxin.setStyleSheet("font: 8pt \"OCR A Extended\";")
        self.checkBoxDarxxin.setObjectName("checkBoxDarxxin")
        self.checkBoxAmoxidex = QtWidgets.QCheckBox(self.frame_2)
        self.checkBoxAmoxidex.setGeometry(QtCore.QRect(210, 490, 111, 20))
        self.checkBoxAmoxidex.setStyleSheet("font: 8pt \"OCR A Extended\";")
        self.checkBoxAmoxidex.setObjectName("checkBoxAmoxidex")
        MainWindow.setCentralWidget(self.centralwidget)

        #Control Plagas
        self.checkBoxTrompa.stateChanged.connect(self.trompa)
        self.checkBoxRidomil.stateChanged.connect(self.ridomil)
        self.checkBoxFullneem.stateChanged.connect(self.fullneem)

        #Control Fertilizante
        self.checkBoxAbimgra.stateChanged.connect(self.abimgra)
        self.checkBoxUrea.stateChanged.connect(self.urea)
        self.checkBoxFosforita.stateChanged.connect(self.fosforita)

        #Antibioticos
        self.checkBoxBenzatinica.stateChanged.connect(self.benzatinica)
        self.checkBoxDarxxin.stateChanged.connect(self.darxxin)
        self.checkBoxRostum.stateChanged.connect(self.rostum)
        self.checkBoxAmoxidex.stateChanged.connect(self.amoxidex)

        self.botonAgregarFactura.clicked.connect(self.validar_campos)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Agregar Propietario"))
        self.labelCedula.setText(_translate("MainWindow", "Cédula Cliente:"))
        self.botonAgregarFactura.setText(_translate("MainWindow", "Agregar Factura"))
        self.labelTitulo.setText(_translate("MainWindow", "CREAR UNA NUEVA FACTURA"))
        self.labelProductosDisponibles.setText(_translate("MainWindow", "Productos Disponibles:"))
        self.checkBoxTrompa.setText(_translate("MainWindow", "TROMPA-Hormiguicida"))
        self.checkBoxRidomil.setText(_translate("MainWindow", "RIDOMIL-Fungicida"))
        self.checkBoxFullneem.setText(_translate("MainWindow", "FULLNEEM-Plagicida"))
        self.labelControlPlagas.setText(_translate("MainWindow", "Control Plagas:"))
        self.checkBoxFosforita.setText(_translate("MainWindow", "FOSFORITA HUILA"))
        self.labelControlPlagas_2.setText(_translate("MainWindow", "Control Fertilizante:"))
        self.checkBoxAbimgra.setText(_translate("MainWindow", "ABIMGRA de gallinaza"))
        self.checkBoxUrea.setText(_translate("MainWindow", "UREA GRANULAR"))
        self.checkBoxRostum.setText(_translate("MainWindow", "ROSTUM"))
        self.labelControlPlagas_3.setText(_translate("MainWindow", "Antibioticos:"))
        self.checkBoxBenzatinica.setText(_translate("MainWindow", "BENZATINICA"))
        self.checkBoxDarxxin.setText(_translate("MainWindow", "DARXXIN"))
        self.checkBoxAmoxidex.setText(_translate("MainWindow", "AMOXIDEX"))

    def trompa(self, estado):
        if estado == Qt.Checked:
            Ui_facturas.listProductos.append('1474')
        elif '1474' in Ui_facturas.listProductos:
            Ui_facturas.listProductos.remove('1474')

    def ridomil(self, estado):
        if estado == Qt.Checked:
            Ui_facturas.listProductos.append('1557')
        elif '1557' in Ui_facturas.listProductos:
            Ui_facturas.listProductos.remove('1557')

    def fullneem(self, estado):
        if estado == Qt.Checked:
            Ui_facturas.listProductos.append('1623')
        elif '1623' in Ui_facturas.listProductos:
            Ui_facturas.listProductos.remove('1623')

    def abimgra(self, estado):
        if estado == Qt.Checked:
            Ui_facturas.listProductos.append('1322')
        elif '1322' in Ui_facturas.listProductos:
            Ui_facturas.listProductos.remove('1322')

    def urea(self, estado):
        if estado == Qt.Checked:
            Ui_facturas.listProductos.append('1525')
        elif '1525' in Ui_facturas.listProductos:
            Ui_facturas.listProductos.remove('1525')

    def fosforita(self, estado):
        if estado == Qt.Checked:
            Ui_facturas.listProductos.append('1738')
        elif '1738' in Ui_facturas.listProductos:
            Ui_facturas.listProductos.remove('1738')
   
    def benzatinica(self, estado):
        if estado == Qt.Checked:
            Ui_facturas.listProductos.append('1345')
        elif '1345' in Ui_facturas.listProductos:
            Ui_facturas.listProductos.remove('1345')

    def darxxin(self, estado):
        if estado == Qt.Checked:
            Ui_facturas.listProductos.append('1678')
        elif '1678' in Ui_facturas.listProductos:
            Ui_facturas.listProductos.remove('1678')

    def rostum(self, estado):
        if estado == Qt.Checked:
            Ui_facturas.listProductos.append('1634')
        elif '1634' in Ui_facturas.listProductos:
            Ui_facturas.listProductos.remove('1634')

    def amoxidex(self, estado):
        if estado == Qt.Checked:
            Ui_facturas.listProductos.append('1346')
        elif '1346' in Ui_facturas.listProductos:
            Ui_facturas.listProductos.remove('1346')

    def validar_campos(self):
        cedula = self.textoCedula.text()

        if not cedula:
            QMessageBox.warning(self, "Campos vacíos", "Por favor, ingrese todos los campos.")
        elif cedula.isdigit():
                datos = {
                        'cedula': cedula
                }
                respuesta = controller_cliente.buscar_cliente(datos)

                if respuesta['success']:
                        factura = controller_facturas.crear_nueva(list(set(Ui_facturas.listProductos)))
                        respuesta = controller_cliente.relacionar_factura(respuesta['cliente'] , factura['factura'])
                        
                        QMessageBox.information(self, "Respuesta", respuesta['mensaje'] + ',\n valor de su compra: ' + factura['valor_total'] )
                else:
                        QMessageBox.warning(self, "Operacion fallida", respuesta['mensaje'] )
                
                Ui_facturas.listProductos = []
                # list(set(Ui_facturas.listProductos))
                self.checkBoxTrompa.setChecked(False)
                self.checkBoxRidomil.setChecked(False)
                self.checkBoxFullneem.setChecked(False)
                self.checkBoxAbimgra.setChecked(False)
                self.checkBoxUrea.setChecked(False)
                self.checkBoxFosforita.setChecked(False)
                self.checkBoxBenzatinica.setChecked(False)
                self.checkBoxDarxxin.setChecked(False)
                self.checkBoxRostum.setChecked(False)
                self.checkBoxAmoxidex.setChecked(False)
                
        else:
                QMessageBox.warning(self, "Error:",'La cédula debe contener solo números')
