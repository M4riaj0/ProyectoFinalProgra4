from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QWidget, QScrollArea
from PyQt5.QtCore import Qt

class VentanaConsultasFacturas(QDialog):
    def __init__(self, facturas):
        super().__init__()
        self.setWindowTitle("Facturas Cliente")
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint) # Quita el signo de interrogación (el logo para pedir ayuda)

        self.resize(666, 780)
        self.setStyleSheet("background-color: rgb(219, 233, 239); font: 10pt 'OCR A Extended';")
        
        # Crear un layout vertical
        layout = QVBoxLayout()

        titulo = QLabel("Facturas")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font: 15pt 'OCR A Extended';")
        layout.addWidget(titulo)

        separador = QLabel('-------------------------------')
        separador.setAlignment(Qt.AlignCenter)
        layout.addWidget(separador)

        # Mostrar la información de las facturas
        for i, factura in enumerate(facturas):

            num_factura = QLabel(f"Factura #{i+1}")
            num_factura.setAlignment(Qt.AlignCenter)
            layout.addWidget(num_factura)

            # Fecha y cantidad de productos
            fecha_productos = QLabel(f"Fecha: {factura['fecha']}")
            fecha_productos.setAlignment(Qt.AlignCenter)
            layout.addWidget(fecha_productos)

            # Cantidad de productos
            cantidad_productos = QLabel(f"Cantidad de productos: {len(factura['productos_control']) + len(factura['antibioticos']) }" )
            cantidad_productos.setAlignment(Qt.AlignCenter)
            layout.addWidget(cantidad_productos)

            # Valor total
            valor_total = factura['valor_total']
            texto_valor_total = QLabel(f"Valor total: {valor_total}")
            texto_valor_total.setAlignment(Qt.AlignCenter)
            layout.addWidget(texto_valor_total)

            # Separador
            separador1 = QLabel('-------------------------------')
            separador1.setAlignment(Qt.AlignCenter)
            layout.addWidget(separador1)

        # Crear un widget y establecer el layout vertical en él
        widget = QWidget()
        widget.setLayout(layout)

        # Crear un QScrollArea y establecer el widget como su contenido
        scroll_area = QScrollArea()
        scroll_area.setWidget(widget)
        scroll_area.setWidgetResizable(True)

        # Establecer el QScrollArea como el layout principal de la ventana
        main_layout = QVBoxLayout()
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)
