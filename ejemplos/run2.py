from mis_clases import Hospital
# Crear dos objetos de la clase 02

# objeto 01
# crear
hospital1 = Hospital("San Agustin", 57, 30, 250000)
# Presentar objeto; usar el método __st__
print(hospital1)

# objeto 02
# crear ingresando valores por teclado
nombre = input("\nIngrese el nombre del hospital: ")
numDoctores = input("Ingrese el numero de doctores que se encuentran en el hospital: ")
numCamas = input("Ingrese el numero de camas que tiene el hospital \""+nombre+"\": ")
presupuesto = input("Ingrese el presupuesto del hospital \""+nombre+"\": ")

hospital2 = Hospital(nombre, numDoctores, numCamas, presupuesto)
# Presentar objeto; usar el método __st__
print(hospital2)

