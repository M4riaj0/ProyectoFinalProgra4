from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_bienvenida(object):
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
        self.labelBienvenido = QtWidgets.QLabel(self.frame_2)
        self.labelBienvenido.setGeometry(QtCore.QRect(220, 230, 151, 20))
        self.labelBienvenido.setStyleSheet("font: 14pt \"OCR A Extended\";")
        self.labelBienvenido.setObjectName("labelBienvenido")
        self.labelSubtitulo1 = QtWidgets.QLabel(self.frame_2)
        self.labelSubtitulo1.setGeometry(QtCore.QRect(190, 320, 221, 20))
        self.labelSubtitulo1.setStyleSheet("font: 10pt \"OCR A Extended\";")
        self.labelSubtitulo1.setObjectName("labelSubtitulo1")
        self.labelSubtitulo2 = QtWidgets.QLabel(self.frame_2)
        self.labelSubtitulo2.setGeometry(QtCore.QRect(140, 360, 331, 20))
        self.labelSubtitulo2.setStyleSheet("font: 10pt \"OCR A Extended\";")
        self.labelSubtitulo2.setObjectName("labelSubtitulo2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 571, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuOpciones = QtWidgets.QMenu(self.menuBar)
        self.menuOpciones.setObjectName("menuOpciones")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionCliente = QtWidgets.QAction(MainWindow)
        self.actionCliente.setObjectName("actionCliente")
        self.actionConsultas = QtWidgets.QAction(MainWindow)
        self.actionConsultas.setObjectName("actionConsultas")
        self.menuOpciones.addAction(self.actionCliente)
        self.menuOpciones.addAction(self.actionConsultas)
        self.menuBar.addAction(self.menuOpciones.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Agregar Propietario"))
        self.labelBienvenido.setText(_translate("MainWindow", "BIENVENIDO"))
        self.labelSubtitulo1.setText(_translate("MainWindow", "Seleccione una opción"))
        self.labelSubtitulo2.setText(_translate("MainWindow", " en la parte superior izquierda"))
