from models.boa_constrictor import Boa_Constrictor
from models.huron import Huron

class Guarderia:
    
    def __init__(self, nombre:str, ubicacion:str) -> None:
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__boas = [
            Boa_Constrictor('pepita', 6.75, 3, 1, 'Salvador', 1700),
            Boa_Constrictor(nombre='pepa pig', peso=5.58, edad=4, kilos_comidos=1, paisorigen='Costa Rica', impuestos=1600)
        ]
        self.__hurones = [
            Huron(nombre='superman', peso=3.85, edad=2, kilos_comidos=1, paisorigen='Mexico', impuestos=1200),
            Huron('batman', 1.85, 1, 1, 'Guatemala', 1950)
        ]
        
    def retornar_nombre(self) -> str:
        return self.__nombre
        
    def retornar_boas(self) -> list:
        return self.__boas
    
    def retornar_hurones(self) -> list:
        return self.__hurones
        
    def alimentar_boa(self,boa:Boa_Constrictor)->str:
        try:
            if isinstance(boa,Boa_Constrictor) == None:
                return "Esta boa no existe!"
            
            boaBuscada = None
            encontroBoa = False
            for boaGuarderia in self.__boas:
                if boa.obtenerNombre() == boaGuarderia.obtenerNombre():
                    boaBuscada = Boa_Constrictor(boaGuarderia.obtenerNombre(), boaGuarderia.obtenerPeso(), boaGuarderia.obtenerEdad(), boaGuarderia.obtener_kilos_comidos(), '', 0.0)
                    encontroBoa = True
            
            if encontroBoa == False:
                return "Esta boa no existe!"
            else:
                try:
                    boaBuscada.adicionar_raton_comido()
                    return "Exito!"
                except ValueError as e:
                    return "La boa esta llena!"
            
        except ValueError as e:
            return f"La boa esta llena!"
        