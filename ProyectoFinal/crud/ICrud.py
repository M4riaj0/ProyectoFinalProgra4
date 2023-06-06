from abc import ABC , abstractmethod

class ICrud ( ABC ) :

    @abstractmethod
    def crear ( self , **kwargs ) :
        raise NotImplementedError

    @abstractmethod
    def obtener ( self , **kwargs ) :
        raise NotImplementedError

    @abstractmethod
    def agregar ( self , **kwargs ) :
        raise NotImplementedError
    
    @abstractmethod
    def consultar ( self , **kwargs ) :
        raise NotImplementedError
    
    # @abstractmethod
    # def actualizar ( self , **kwargs ) :
    #     raise NotImplementedError
    
    # @abstractmethod
    # def eliminar ( self , **kwargs ) :
    #     raise NotImplementedError