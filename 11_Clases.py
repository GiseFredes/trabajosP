######## Clases #######
class MiPersonaVacia:
    pass  #Indica que la clase esta vacia

print(MiPersonaVacia)
print(MiPersonaVacia())

###Lo anterior es simple ejemplos, en la realidad si esta vacia es muy inutil la clase

class Persona:
    #Constructor de clase, me permite crear la clase
    def __init__(self, name, surname, alias="Sin Alias"):
        #self.name=name   #Aca asigno las variables y creo las variables
        #self.surname=surname
        #Otra forma
        self.full_name=f"{name} {surname} ({alias})"  #Propiedad pública
        self.__name=name  #Propiedad privada
        self.__surname=surname

    #Definimos metodos
    def walk(self):
        print(f"{self.full_name} está caminando")
    def get_name(self):
        return self.__name


my_person=Persona("Camila", "Rivas")
#print(my_person.name)
print(f"La clase que acaabo de crear jej)")#{my_person.name} {my_person.surname}")
#Segunda forma ejemplo
print(my_person.full_name)
my_person.walk()

my_other_person=Persona("Maxi","Rivas", "PAvotito")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name= "Gisela Fredes (Vieja)"
my_other_person.walk()
my_other_person.full_name=678
print(my_other_person.full_name)

