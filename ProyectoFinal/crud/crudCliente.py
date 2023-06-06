import ICrud
import sys
import os
path = os.path.abspath('Model/')
sys.path.append(path)
import cliente 
    
class CrudCliente ( ICrud.ICrud ) :
    def __init__(self):
        self.clientes = []

    def crear(self, **kwargs):
        nuevo_cliente = cliente.Cliente(kwargs['nombre'], kwargs['cedula'])
        self.clientes.append(nuevo_cliente)
        mensaje = "El cliente se ha creado exitosamente"
        return {'mensaje': mensaje, 'cliente_nuevo': nuevo_cliente}

    def agregar(self, **kwargs):
        factura = kwargs.get('factura')
        cliente = kwargs.get('cliente')
        if cliente and factura:
            cliente.facturas.append(factura)
            mensaje = "Factura agregada exitosamente"
        else:
            mensaje = "No se ha proporcionado cliente o factura"
        return {'mensaje': mensaje}

    def obtener(self, cliente):
        if cliente:
            facturas = cliente.facturas
            return {'cliente': cliente, 'facturas': facturas}
        else:
            return {'mensaje': "No se ha proporcionado cliente"}

    def consultar(self, **kwargs):
        cedula = kwargs.get('cedula')
        if cedula:
            for c in self.clientes:
                if c.cedulaCliente == cedula:
                    datos = {'cliente': c, 'success' : True, 'mensaje': 'El cliente ya existe'}
                    return datos
            mensaje = "No se ha encontrado este cliente"
        else:
            mensaje = "No se ha proporcionado cédula"
        return {'mensaje': mensaje , 'success' : False}

    def actualizar(self, **kwargs):
        cedula = kwargs.get('cedula')
        nuevo_nombre = kwargs.get('nuevo_nombre')
        if cedula and nuevo_nombre:
            for c in self.clientes:
                if c.cedulaCliente == cedula:
                    c.nombreCliente = nuevo_nombre
                    mensaje = 'Cliente actualizado exitosamente'
                    return {'mensaje': mensaje}
            mensaje = 'No se ha encontrado este cliente'
        else:
            mensaje = 'No se ha proporcionado cédula o nuevo_nombre'
        return {'mensaje': mensaje}

    def eliminar(self, **kwargs):
        cedula = kwargs.get('cedula')
        if cedula:
            for c in self.clientes:
                if c.cedulaCliente == cedula:
                    self.clientes.remove(c)
                    mensaje = 'Cliente eliminado exitosamente'
                    return {'mensaje': mensaje}
            mensaje = 'El cliente no existe'
        else:
            mensaje = 'No se ha proporcionado cédula'
        return {'mensaje': mensaje}

    def consultarFacturas(self, **kwargs):
        cedula = kwargs.get('cedula')

        for c in self.clientes:
            if c.cedulaCliente == cedula:
                datos = {'cliente': c,}
                return datos
