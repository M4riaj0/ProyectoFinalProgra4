class Antibioticos:
    def __init__(self, registroICA, nombreProducto, dosisKg, tipoAnimal, precio):
        if registroICA is None and nombreProducto is None and dosisKg is None and  tipoAnimal is None and  precio is None:
            raise TypeError('No se ingresaron los atributos')
        if nombreProducto=='' or dosisKg=='' or tipoAnimal=='' or precio=='':
            raise(TypeError('Los campos están vacíos'))
        if not nombreProducto.replace(" ", "").isalpha():
                raise ValueError('El nombre del producto debe contener solo letras')
        if not (tipoAnimal=='bovinos' or tipoAnimal=='caprinos' or tipoAnimal=='porcinos' or tipoAnimal=='bovino' or tipoAnimal=='caprino' or tipoAnimal=='porcino') :
                raise ValueError('Recuerde que los tipos de animales son: Bovinos, Caprinos, Porcinos')
        try:
            valor_dosis = int(dosisKg)
            valor_precio = int(precio)
        except ValueError:
            raise(ValueError('El dato debe contener solo números')) 

        self.__registroICA = registroICA
        self.__dosisKg = dosisKg
        self.__nombreProducto = nombreProducto
        self.__tipoAnimal = tipoAnimal
        self.__precio = precio

    @property 
    def registroICA(self):
        return self.__registroICA
    
    @property 
    def nombreProducto(self):
        return self.__nombreProducto
    
    @nombreProducto.setter
    def nombreProducto(self, nuevoNombre):
        self.__nombreProducto = nuevoNombre
    
    @property 
    def dosisKg(self):
        return self.__dosisKg
    
    @dosisKg.setter
    def dosisKg(self, nuevaDosis):
        self.__dosisKg = nuevaDosis

    @property 
    def tipoAnimal(self):
        return self.__tipoAnimal
    
    @tipoAnimal.setter
    def tipoAnimal(self, cambiarTipo):
        self.__tipoAnimal = cambiarTipo

    @property 
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, nuevoValor):
        self.__precio = nuevoValor

    

#pytest test\test_antibioticos.py  Así se pone en el terminal para revisar si funcionan los test