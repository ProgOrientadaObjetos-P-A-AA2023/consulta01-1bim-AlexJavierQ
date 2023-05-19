
# Crear dos clases en Python
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01
class Automovil:

    def __init__(self,marca,modelo, color, origen):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.origen = origen

    def __str__(self):
        return(f"\nDatos para la matricula de un vehiculo \n"
              f"Marca del vehiculo: {self.marca}\n"
              f"Modelo del vehiculo: {self.modelo}\n"
              f"Color del vehiculo: {self.color}\n"
              f"Importado desde: {self.origen}")


# clase 02
class Hospital:
    def __init__(self,nombre, numDoctores, numCamas, presupuesto):
        self.nombre = nombre
        self.numDoctores = numDoctores
        self.numCamas = numCamas
        self.presupuesto = presupuesto

    def __str__(self):
        return(f"\nDatos del Hospital \"{self.nombre}\":\n"
              f"Cuenta con un personal medico de {self.numDoctores} doctores\n"
               f"Cuenta con un total de {self.numCamas} camas\n"
              f"Tiene un presupuesto de ${self.presupuesto} dolares")
