#############LISTAS#############
print("***************************")
print("Listas")
my_list = list()#definimos una lista base
my_other_list=[]#Otra lista base
print("Funcion len")
print(len(my_list)) #Devuelve 0 porque es la cantidad de elementos
print("***************************")

my_list=[35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))
print("***************************")

print("Funcion Tipo")
my_other_list=[35, 1.77, "Brais", "Moure"]# No es necesario que sean el mismo tipo de datos
print(type(my_other_list))#Tipo lista

print("***************************")
print("Imprimimos por lugar")
print(my_list[0])
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
#print(my_other_list[-5])#No existe este elemento
#print(my_other_list[4]) Tampoco este elemento esta
print("***************************")
print("Metodo count")
print(my_other_list.count("Brais"))#Devuelve el numero de ocurrencias
print(my_list.count(30))
print("***************************")

#Ahora le puedo poner nombre a las variables
#guardadas en my_other_list
#Se nombran todas las variables sino da error
print("Nombrar variables; muy rebuscado, posibles errores")
age, height, name, surname= my_other_list
print(age)
#Si se los puede nombrar con distinto orden
name, age, height, surname= my_other_list[2], my_other_list[0],my_other_list[1],my_other_list[3]
print(name, age, height)
################
print("***************************")
print("Operaciones con Listas")
print(my_list + my_other_list)
print(my_other_list + my_list)
#print(my_list - my_other_list)
#print(my_list * my_other_list)
#no son operaciones validas 
################
print("***************************")
print("Tipado dinamico-Se asigna valor a la variable durante la ejecucion")
#print(list([1,2,3,4]))#Para asignarle el tipo list
#segunda opcion sin el constructor de lista
print([1,2,3,4])
#my_list="Hola Mundo"
print(my_list)
print(type(my_list))#Ya no es más lista
#Ojo problemas de tipo
#No se puede crear constantes en python

print("***************************")
print("Metodo append, agregar un elemento")
my_other_list.append("Maurodev")#Inserta un elemento siempre al final de la lista
print(my_other_list)
print("Metodo insert, agregar un elemento")
my_other_list.insert(1, "Azul")#Inserta un elemento en la posición indicada
print(my_other_list)
print("Metodo remove, borrar un elemento")
print(my_other_list.remove("Azul"), "Aca no hay devolucion como en el metodo pop")
print(my_other_list)
my_list.remove(30)
print(my_list)
print("Metodo pop elimina el ultimo elemento")

print(my_list.pop()," elemento eliminado")
print(my_list)

print(my_list.pop(2)," elemento eliminado")
print(my_list)
my_new_list=my_list.copy()
print("Utilizamos del")

del my_list[2]
print(my_list)
print("Utilizamos clear")
my_list.clear()
print(my_list, "Lista despues del clear")
print(my_new_list, "La guarde aca")
my_new_list.reverse()
print(my_new_list, "despues del reverse, da vuelta los datos")
my_new_list.sort()
print(my_new_list,"Despues del sort, ordena los elementos")
print("##################################################")
print("Sublistas")
#Para trabajar mejor los ejemplos agrego 4 elementos a la lista
my_new_list.append(5)
my_new_list.append(6)
my_new_list.append(7)
my_new_list.append(8)
print(my_new_list)
print(my_new_list[1:2])
print(my_new_list[2:6])
print(my_new_list[7:2])#En reversa no va


print("*******************Fin***********************")