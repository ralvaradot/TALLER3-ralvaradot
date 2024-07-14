from abc import ABC, abstractmethod
from models.ianimal import IAnimal

class Animal(IAnimal, ABC):
    def __init__(self, nombre:str, peso: float, edad:int, kilos_comidos:int)->None:
        self.__nombre= nombre
        self.__peso = peso
        self.__edad = edad
        self.__kilos_comidos = kilos_comidos
        
    @abstractmethod
    def hacer_sonido(self)->str:
        pass
    
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerPeso(self)->float:
        return self.__peso
        
    def obtenerEdad(self)->int:
        return self.__edad
    
    def comer(self, kilos:int)->None:
        self.__kilos_comidos += kilos
    
    def obtener_kilos_comidos(self)->int:
        return self.__kilos_comidos