from models.guarderia import Guarderia
from models.boa_constrictor import Boa_Constrictor
from models.huron import Huron

guarderia = Guarderia("Las Boas de Bogota", "Bogota-Colombia")

print("Guarderia: " , guarderia.retornar_nombre())
print("-------------------------------")
print("Presentamos nuestras boas: ")
print("-------------------------------")
for boa in guarderia.retornar_boas():
    print("Nombre boa: ",boa.obtenerNombre())
    print("Edad boa: ",boa.obtenerEdad())
    print("Peso de boa: ",boa.obtenerPeso())
    print("-------------------------------")

print("Presentamos nuestros hurones: ")
print("-------------------------------")
for huron in guarderia.retornar_hurones():
    print("Nombre huron: ",huron.obtenerNombre())
    print("Edad huron: ",huron.obtenerEdad())
    print("Peso de huron: ",huron.obtenerPeso())
    print("-------------------------------")
    
print("==============================")
print("Alimentacion de las Boas")
print("-------------------------------")
boa1 = Boa_Constrictor('pepita', 6.75, 3, 1, 'Salvador', 1700)
guarderia.alimentar_boa(boa1)
for i in range(11):
    print(guarderia.alimentar_boa(boa1))

print('----------------------------------')    
print('Nueva boa boricua ')
boa2 = Boa_Constrictor("boricua", 4.67, 7, 3,'Colombia', 1250)  
print('intento de alimentar a la boa boricua ') 
print(guarderia.alimentar_boa(boa2) )
