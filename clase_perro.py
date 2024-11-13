#clase y objeto II

class Perro:
    def __init__(self,nombre,peso,edad):
        self.nombre = nombre
        self.peso = peso
        self.edad = edad
        self.comida = []
        self.registro_medico = {}

    def ladra(self):
        print(f"Guauu!!")
    
    def mostrar_datos_perro(self):
        print(f"El nombre es {self.nombre}, pesa {self.peso}kg, y su edad es {self.edad}")

    def agregar_comida(self,alimento):
        #Agrega un alimento a la lista de comidas favoritas del perro
        self.comida.append(alimento)
        print(f"'{alimento}' ha sido agregado a la lista de comidas favoritas de {self.nombre}")

    def mostrar_comida(self):
        if self.comida:
            print(f"La comidad favorita de {self.nombre} es {', '.join(self.comida)}")
        else:
            (f"no hay alimentos agregados")

    
    def agregar_registro_medico(self,fecha,descripcion):
        self.registro_medico[fecha] = descripcion
        print(f"Se ha agregadi el registro medico en la fecha {fecha} para {self.nombre}")
    
    def mostrar_registro_medico(self):
        if self.registro_medico:
            print(f"Historial medico de {self.nombre}")

            for fecha, descripcion in self.registro_medico.items():
                print(f"{fecha} : {descripcion}")
        else:
            print(f"{self.nombre} no tiene registro medico")

#-----------------------------------------------------------#
#creo el objeto first_dog y se cargan los datos instanciados
first_dog = Perro('lupita',30,4)

#se muestra los datos de la clase perro
first_dog.mostrar_datos_perro()

#se prueba la funcion de ladrar de la clase perro
first_dog.ladra()

#se hace uso de la funcion de agregar comida
first_dog.agregar_comida("pollito")
first_dog.agregar_comida("manzana")
first_dog.agregar_comida("pan")
first_dog.agregar_comida("doc selection")

#se solicita mostrar la comida agregada
first_dog.mostrar_comida()

#se agrega un registro medico para el animal
first_dog.agregar_registro_medico("14/05/2024","Desparasitario")
first_dog.agregar_registro_medico("25/06/2024", "Vacuna Antirabica")
first_dog.agregar_registro_medico("10/02/2024", "Pipeta para garrapatas")
first_dog.mostrar_registro_medico()
#-----------------------------------------------------------#
print("-----------------------------------------")
#-----------------------------------------------------------#

second_dog = Perro("Tina",20,3)

second_dog.ladra()

second_dog.mostrar_datos_perro()

second_dog.agregar_comida("arroz")
second_dog.agregar_comida("doc selection")
second_dog.agregar_comida("carne")
second_dog.agregar_comida("pescado")

second_dog.agregar_registro_medico("12/01/2018", "Primera vacuna")
second_dog.agregar_registro_medico("13/02/2018", "Segunda Vacuna")
second_dog.agregar_registro_medico("17/03/2018", "Vacuna antirabica")
second_dog.agregar_registro_medico("25/02/2019", "Zoonosis 'Castracion' ")

second_dog.mostrar_registro_medico()