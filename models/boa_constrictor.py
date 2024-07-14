from models.animalExotico import AnimalExotico
 
class Boa_Constrictor(AnimalExotico):
    
    def __init__(self,nombre:str, peso:float, edad:int, kilos_comidos:int, paisorigen:str, impuestos:float)-> None:
        super().__init__(nombre, peso,edad, kilos_comidos, paisorigen, impuestos)
        self.__ratonesComidos = 0
    
    def hacer_sonido(self) -> str:
        return "¡Tssss!"
    
    def adicionar_raton_comido(self)->str:
        if self.__ratonesComidos == 10:
            raise ValueError("Demasiados Ratones!!")
        self.__ratonesComidos += 1
        return ""
        
    def obtenerRatonesComidos(self) -> int:
        return self.__ratonesComidos
