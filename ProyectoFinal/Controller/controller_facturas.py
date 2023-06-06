from datetime import datetime
import sys
import os
path = os.path.abspath('stock/')
sys.path.append(path)
import productos
path = os.path.abspath('crud/')
sys.path.append(path)
import crudFactura

crud_factura = crudFactura.CrudFacturas()

def crear_nueva(pedido):
    factura = crud_factura.crear()
    productos_disponibles_object = productos.generar_productos()
    productos_disponibles = crud_factura.consultar(productos_disponibles_object)
    for producto in pedido:
        if producto in productos_disponibles:
            posicion = productos_disponibles.index(producto)
            solicitud = productos_disponibles_object[posicion]
            # print('solicitud: ' , solicitud)
            factura = crud_factura.agregar(**{'factura': factura , 'producto': solicitud})
    resultado = crud_factura.obtener([factura])
    # print('factura total: ', resultado[0])
    return {'factura': factura , 'valor_total': resultado[0]['valor_total'] }

def leer_facturas(facturas):
    resultado = crud_factura.obtener(facturas)
    return resultado
    


