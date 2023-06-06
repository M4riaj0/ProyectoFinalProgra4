from productos_control import ProductosControl
from control_plagas import ControlPlagas
from antibioticos import Antibioticos

class Facturas:
    def __init__(self, fechaFactura):

        if fechaFactura == '':
            raise TypeError('El campo está vacío')

        self.__fechaFactura = fechaFactura
        self.__ProductosControl = []
        self.__antibioticos = []
    
    @property
    def fechaFactura(self):
        return self.__fechaFactura
    
    @fechaFactura.setter
    def fechaFactura(self, nuevaFecha):
        self.__fechaFactura = nuevaFecha

    @property
    def ProductosControl (self):
        return self.__ProductosControl
    
    @ProductosControl.setter
    def ProductosControl (self, nuevoProducto):
        self.__ProductosControl.append(nuevoProducto)

    @property
    def antibioticos (self):
        return self.__antibioticos
    
    @antibioticos.setter
    def antibioticos (self, nuevoAntibiotico):
        self.__antibioticos.append(nuevoAntibiotico)

    @property
    def valorTotal(self):
        valor = 0
        for producto in self.__ProductosControl:
            valor = valor + producto.valorProducto
        for antibiotico in self.__antibioticos:
            valor = valor + int(antibiotico.precio)
        return valor
    
    
