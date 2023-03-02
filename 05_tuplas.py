################Tuplas#####################
print("###########################################")
print("Tuplas")

my_tupla=tuple()
my_other_tupla=(30, 60, 35)
print("###########################################")
my_tupla = (35, 1.77, "Brais", "Mauro","Brais")
print(my_tupla)
print(type(my_tupla))
print("###########################################")
print(my_tupla[0], "Indice 0")
print(my_tupla[-1], "Indice -1, igual a ultimo elemento")
#print(my_tupla[4]) Error
#print(my_tupla[-6]) Error

print("###########################################")

print(my_tupla.count("Brais"))#Cuenta la cantidad de coincidencias  

print(my_tupla.index("Mauro"))#La busqueda deber ser precisa
#El índice del elemento buscado
print("###########################################")
print(my_tupla.index("Brais"))#Se queda con la primera coincidencia
#Las anteriores son las únicas dos operaciones que tienen las tuplas
#my_tupla[1]=1.80
#my_tupla[5]=1.80
print(my_tupla)

#En el momento de crear defino los datos y no los puedo modificar después
print("###########################################")
my_sun_tupla=(my_tupla + my_other_tupla)
print(my_sun_tupla)
print(my_sun_tupla[3:6])
print("###########################################")
my_tupla=list(my_tupla)    #La transforme en lista          
print(type(my_tupla))
my_tupla[4]= "MauroDev"
print(my_tupla)
my_tupla.insert(1, "Azul")#Operaciones con lista
my_tupla=tuple(my_tupla)
print(type(my_tupla))#Esto da seguridad no permitir cambios externos
print("###########################################")
#del my_tupla[2]No se permite borra toda la tupla no
del my_tupla
#print(my_tupla)nos da error porque la tupla no existe






