from abc import ABC, abstractmethod

class IAnimal(ABC):
    @abstractmethod
    def comer(self, kilos:int)->None:
        pass
    
    @abstractmethod
    def obtener_kilos_comidos(self)->int:
        pass
    
    