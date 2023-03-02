#VARIABlES
my_string_variable = ('Mi primera cadena')
print(my_string_variable)

my_int_variable = 88
print(my_int_variable)

my_bolean_variable = False
print(my_bolean_variable)


#Variables en una sola línea. Cuidado con el abuso de esta sintaxis
name, surname, nickname, age= 'Gisela', 'Fredes','GiFredes', 43
print("Mi nombre es", name, "mi apellido es", surname, "mi edad es", age, "Mi sobrenombre es:",nickname)


# El print acepta multiplesargumentos separados por coma

print(my_bolean_variable, my_int_variable, my_string_variable)




'''*******************************************
**********************************************
********Empezamos con las funciones***********'''

# Funcion Str, transfoma el entero en una cadena
my_int_to_string_variable =str(my_int_variable)
print(my_int_to_string_variable)
print(type(my_int_to_string_variable))

#Concatenar variables en un print
'''
Para concatenar un numero a un string se debe hacer uso de la funcion 
str() o usar alguna de las siguientes formas de concatenar

Usando la funcion format de los strings:

print("{}, World".format(saludo))
La funcion format no solo permite concatenar sino que posee mas “Habilidades” que pueden ser muy utiles en algunas ocasiones
https://pyformat.info/'''
saludo = "Hello"
#Usando el simbolo de adicion:
print(saludo + ", World")
#print(saludo + 5), Error no se concatena enteros con str

# Usando format se puede concatenar no solo strings sino tambien numeros
print("{}, World".format(saludo))

#Usando f strings
saludo = "Hello"
print(f"{saludo}, World")# Con f pongo entre llaves las variables

print(f"{9 * 8}")#Pongo mlos enteros y me da el resultado

#Definamos una funcion, que transfome en mayuscula
def uppercase(string):#.upper transfoma a mayuscula
	return string.upper()#Uppercase es el nombre de la funcion

print(f"{uppercase('mayusculas')}")
#El print llama a la funcion 
#Usando una f (mayuscula o minuscula) justo antes del string que queremos formatear, es posible usar variables, realizar operaciones y ejecutar codigo de Python dentro de las llaves.

#Funcion len
'''Puede pasar a la función len() un valor 
de cadena (o una variable que contenga una cadena), y la función
evalúa el número de caracteres que contiene la cadena.'''
miNombre = 'carlos'
print('La longitud de tu nombre es:')
print(len(miNombre))

#Funcion input()
'''El objetivo de la instrucción input es parar un programa en Python,
esperar que el usuario introduzca un dato mediante el teclado, y tras 
apretar la tecla enter (o intro o return), almacenar este dato en una 
variable.'''
edad_1 = int(input('Teclear edad: '))  # entrada de entero
peso_1 = float(input('Teclear peso: '))  # entrada de flotante
nombre_1 = input('Teclear nombre: ')  # entrada de cadena
print(nombre_1, edad_1, 'años', peso_1, 'kg')  # muestra datos



#####Puedo cambiar las va5riables y los tipos de variables
miNombre='Pedro'
print(miNombre)

miNombre=45
print(miNombre)#no tiene problemas con que le cambiemos los typos
#Ojo, puede provocar grandes problemas, cuidado

