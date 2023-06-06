import sys
import os
path = os.path.abspath('crud/')
sys.path.append(path)
import crudCliente

crud_cliente = crudCliente.CrudCliente()

def crear_cliente(datos):
    existente = crud_cliente.consultar(**datos)
    
    if existente['success']:
        return {'mensaje': existente['mensaje'] , 'success' : False}
    else:
        crear_nuevo = crud_cliente.crear(**datos)
        return {'mensaje': crear_nuevo['mensaje'] , 'success' : True}

def buscar_cliente(datos):
    existente = crud_cliente.consultar(**datos)
    return existente

def relacionar_factura(cliente, factura):
    mensaje = crud_cliente.agregar(**{'cliente': cliente , 'factura': factura})
    return mensaje

def buscar_facturas(cliente):
    respuesta = crud_cliente.obtener(cliente)
    return respuesta

def eliminar_cliente(datos):
    respuesta = crud_cliente.eliminar(**datos)
    return respuesta