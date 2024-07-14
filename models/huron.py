from models.animalExotico import AnimalExotico
 
class Huron(AnimalExotico):
    
    def __init__(self,nombre:str, peso:float, edad:int,kilos_comidos:int,  paisorigen:str, impuestos:float)-> None:
        super().__init__(nombre, peso,edad,kilos_comidos, paisorigen, impuestos)
        
    
    def hacer_sonido(self) -> str:
        return "¡Eek Eek!"