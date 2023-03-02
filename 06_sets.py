##########  SETS #############

my_set= set()
my_other_set={}
print(type(my_set))
print(type(my_other_set))#inicialmente es un diccionario

my_other_set={"Gisela", "Fredes", 43}
#este es un set por la forma de ingresar datos
#recordar que pyton es de tipado debil

print(type(my_other_set))

print(len(my_other_set))
#estan ordenados, distintos a como  los cargue
#print(my_other_set[0])Esto da error
print(my_other_set)
my_other_set.add("Camila")#Solo se puede agregar un elemnto
print(my_other_set)#Ordena como quiere
my_other_set.add("Camila")
print(my_other_set)#No admite repetidos

print("Gisela" in my_other_set)
#Determina si el elemnyo esta en el set
print("Gisla" in my_other_set)

my_other_set.remove("Gisela")
#ELimina el elemento

print(my_other_set)
my_other_set.clear()
#Elimina todos los elemntos de la lista
print(my_other_set,"Jejeje")
del my_other_set#Elimina el set
#print(my_other_set) No existe mas el set
my_set={"Gisela","Fredes", 43}
my_other_set={"HTML", "CSS", "PYTHON","JAVASCRIPT"}
my_new_set= my_set.union(my_other_set)
print(my_new_set)
my_new_set=my_new_set.union({"JAVA","C#"})
print(my_new_set,"JEJEJEJ")

print(my_other_set.difference(my_set))








