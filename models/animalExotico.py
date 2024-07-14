from models.animal import Animal
from abc import ABC, abstractmethod

class AnimalExotico(Animal):
    
    def __init__(self, nombre:str, peso:float, edad:int, kilos_comidos:int, paisOrigen:str, impuestos:float)->None:
        super().__init__(nombre,peso,edad,kilos_comidos)
        self.__paisOrigen = paisOrigen
        self.__impuesto = impuestos

    def calcular_flete(self)->float:
        return self.__impuesto * self.obtenerPeso()
 
    @abstractmethod
    def hacer_sonido(self)->str:
        pass
    
    