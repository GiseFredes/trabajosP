#######String##########

my_string='Mi String'
my_other_string='Mi String'

print(len(my_string))
print(len(my_other_string))

print(my_string+' '+my_other_string)


my_new_line_string="Este es un string\ncon un salto de línea"

print(my_new_line_string)

my_tab_string="\tEste es un string con tabulación"

print(my_tab_string)

my_escapado_string='\t Este es un string \n escapado'
print(my_escapado_string)

my_escapadossss_string='\\t Este es un string \\n escapado'
print(my_escapadossss_string)


#***************Formateo*******************
name, surname, age = "Gisela", "Fredes", 43

print("mi nombre es: "+ name + " mi apellido es: " + surname+ " y mi edad: " + str(age))
#Esta es la forma que se nos viene primero a la mente
#Pero es muy lenta y hay mejores
print('Mi nombre es %s, mi apellido es %s y mi edad %d'%(name, surname, age))
print(f"mi nombre es {name}, mi apellido {surname}, y mi edad {age}")
print("Prrobando 3 {} {} y {}".format(name, surname, age))
#listo me dieron las tres formas
#Prefiero la segunda, se llamam interpolación, porque la use hasta ahora

#******Desenpaquetado de paquetes*********
lenguaje= "Python"
a, b, c, e, f, g= lenguaje
#Asi cada una de las letras de la palabra se separan
print(a, c)
print(b)
print(g, b)

#******************Division*******************
languaje_slice= lenguaje[1:3]
print(languaje_slice)

languaje_slice= lenguaje[0:6:2]
print(languaje_slice)

languaje_slice= lenguaje[-3]
print(languaje_slice)

#*******************Reverse***********************
reverse_languaje= lenguaje[::-1]#invierte el orden de la cadena
print(reverse_languaje)

#*****************Funciones*****************

print(lenguaje.upper())#Todas en mayuscula
print(lenguaje.capitalize())#La primera en mayuscula
print(lenguaje.count("t"))#cuantas coincidencias hay en la cadena
print(lenguaje.isnumeric())#Es un número
print("1".isnumeric())#para ver la diferencia
print(lenguaje.lower())#Todas en minuscula
print(lenguaje.upper().isupper())#La convierte en mayuscula y pregunto si es mayuscula
print(lenguaje.lower().isupper())
print(lenguaje.startswith("Py"))#Comienza con py


