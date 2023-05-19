from mis_clases import Automovil
# Crear dos objetos de la clase 01

# objeto 01
# crear
vehiculo1 = Automovil("Chevrolet", "Vitara", "Azul", "Canada")
# Presentar objeto; usar el método __st__
print(vehiculo1)

# objeto 02
# crear ingresando valores por teclado
marca = input("\nIngrese la marca del vehiculo: ")
modelo = input("Ingrese el modelo del vehiculo: ")
color = input("Ingrese el color del vehiculo: ")
origen = input("Ingrese desde donde se importo el vehiculo: ")

vehiculo2 = Automovil(marca, modelo, color, origen )
# Presentar objeto; usar el método __st__
print(vehiculo2)

