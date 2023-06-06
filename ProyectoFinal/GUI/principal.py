from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QDialog
from Ui_ventana_bienvenida import Ui_bienvenida
from Ui_ventana_cliente import Ui_cliente
from Ui_ventana_facturas import Ui_facturas

class VentanaCliente(QMainWindow, Ui_cliente):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class VentanaFacturas(QMainWindow, Ui_facturas):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class VentanaPrincipal(QMainWindow, Ui_bienvenida):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Crear acciones del menú
        self.actionCliente = QAction("Cliente", self)
        self.actionCliente.triggered.connect(self.mostrar_ventana_cliente)
        self.actionConsultas = QAction("Facturas", self)
        self.actionConsultas.triggered.connect(self.mostrar_ventana_consultas)

        # Agregar acciones al menú
        self.menuBar.addAction(self.actionCliente)
        self.menuBar.addAction(self.actionConsultas)

    def mostrar_ventana_cliente(self):
        self.cliente_window = VentanaCliente()
        self.setCentralWidget(self.cliente_window)

    def mostrar_ventana_consultas(self):
        self.consultas_window = VentanaFacturas()
        self.setCentralWidget(self.consultas_window)

if __name__ == "__main__":
    app = QApplication([])
    main_window = VentanaPrincipal()
    main_window.setWindowTitle("Sistema de facturación")
    main_window.show()
    app.exec_()
