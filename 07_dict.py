######DICCIONARIOS######
 
my_dicc= dict();
my_other_dicc={};


print(type(my_dicc));
print(type(my_other_dicc));

my_other_dicc={"Nombre":"Gisela", "Apellido":"Fredes","Edad":43, 1:"Pytont"}

my_dicc={"Nombre":"Maxi","Apellido":"Rivas", "Edad":10 ,"Lenguaje":{"Python","Java","Sql"}, 1:1.73}

print(my_other_dicc)

print(my_dicc)
print("Largo de my_other dicc:", len(my_other_dicc))
print("el largo de my_dicc es:",len(my_dicc))
#Puedo acceder por clave
print(my_dicc["Nombre"])

my_dicc["Nombre"]="Camila"

print(my_dicc["Nombre"])
#print(my_dicc["1"])   Error es un entero no un alfanumerico

print(my_dicc[1])
my_dicc["calle"]="Alem 959"


print(my_dicc)
del my_dicc["calle"]
print(my_dicc)
print("Camila" in my_dicc) #Falso porque busca por clave
print("Apellido" in my_dicc)
#print(my_dicc.clear())   SOlo lo hago para probar funciona

#Devuelve el diccionario como una lista
#de item clave valor
print(my_dicc.items())
#Devuelve las claves del diccionario
print(my_dicc.keys())
#Esta funcion me devuelve los valores de la funcion
print(my_dicc.values())

my_list=["Nombre", 1, "Piso"]
#La siguiente funcion utiliza los valores de la lista
#para crear la claves en el diccionario nuevo

my_New_Dict= dict.fromkeys(my_list)
#Como utilice solo una lista, esta se toma como claves
#Todos los valores creados seran null
#Puedo colocar otra lista que tomaran sus valores o cargarlos manualmente
#dict.fromkeys(Clave, Valor)
dicci=dict.fromkeys(("Raza","Color","Peso"),("Cooker", "Marron", 3.40))
#Fijate que asi tampoco lo carga como yo quiero
dicci=dict.fromkeys(("Raza","Color","Peso"),("Cooker", "Marron", 3.40))






