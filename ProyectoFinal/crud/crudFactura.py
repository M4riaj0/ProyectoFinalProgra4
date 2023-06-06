from datetime import datetime
import ICrud
import sys
import os
path = os.path.abspath('Model/')
sys.path.append(path)
import facturas
import control_plagas
import fertilizantes
import antibioticos

class CrudFacturas ( ICrud.ICrud ):

    def crear(self):
        nueva_factura = facturas.Facturas(datetime.now().strftime("%Y-%m-%d"))
        return nueva_factura

    def agregar(self, **kwargs):
        if isinstance(kwargs['producto'], antibioticos.Antibioticos):
            kwargs['factura'].antibioticos.append(kwargs['producto'])
        else:
            kwargs['factura'].ProductosControl.append(kwargs['producto'])
        return kwargs['factura']

    def obtener(self, facturas):
        factura_dict_list = []
        count = 1
        for factura in facturas:
            factura_dict = {}
            factura_dict["factura"] = count
            factura_dict["fecha"] = factura.fechaFactura
            factura_dict["productos_control"] = []
            for producto in factura.ProductosControl:
                producto_dict = {
                    "nombre": producto.nombreProducto,
                    "valor": producto.valorProducto
                }
                factura_dict["productos_control"].append(producto_dict)
            factura_dict["antibioticos"] = []
            for antibiotico in factura.antibioticos:
                antibiotico_dict = {
                    "nombre": antibiotico.nombreProducto,
                    "precio": antibiotico.precio,
                    "tipo_animal": antibiotico.tipoAnimal
                }
                factura_dict["antibioticos"].append(antibiotico_dict)
            factura_dict["valor_total"] = str(factura.valorTotal)
            factura_dict_list.append(factura_dict)
            count += 1

        return factura_dict_list

    def consultar (self, ListProductos):
        newList = []
        for producto in ListProductos:
                newList.append(str(producto.registroICA))
        return newList

