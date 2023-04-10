######## Bucles  #########

# While
my_condition=0

while my_condition<10:
    print(my_condition)
    my_condition+=2
else:
    print("Es mayor o igual que diez")
#Esto es solo de phyton  

while my_condition<20:
    my_condition+=1
    if my_condition==15:
        print("La condicion es igual a 15")  
        break
    print(my_condition)

print("La ejecucion continua")

#######   FOR  #######

my_list=[35, 24, 62, 52, 30, 30, 17]
print("Imprimimos la lista con un for:")

for element in my_list:
    print(element)

my_dicc={"Nombre":"Gisela","Apellido":"Fredes","Edad":43, 1:1.68}
my_tupla = (35, 1.77, "Brais", "Mauro","Brais")
my_set={"HTML", "CSS", "PYTHON","JAVASCRIPT"}

print("Imprimimos el diccionario con un for:")

for element in my_dicc:
    print(element)

print("Imprimimos el set con un for:")

for element in my_set:
    print(element)

print("Imprimimos la tupla con un for:")

for element in my_tupla:
    print(element)
    


