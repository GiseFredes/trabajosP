############# Funciones ############

#Funcion básica sin parametros

def my_Function():
    print("Esto es una funcion")

my_Function()
my_Function()

#Función con parametros y no devuelve nada
def suma_Dos_Valores(primero, segundo):
    print(primero+segundo)

suma_Dos_Valores(15,20)
suma_Dos_Valores(556,852)
#Como python no es de tipado estricto y el más tambien funciona como concatenacion
suma_Dos_Valores("43","F")
#Funcion con paametro retornando un valor

def suma_Con_Retorno(primero, segundo):
    return primero+segundo

resultado=suma_Con_Retorno(9,4)
print(resultado)

def imprime_Nombre(nombre, apellido):
    print(f"{nombre} {apellido}")

imprime_Nombre("Gisela","Fredes")

#Funciones en la cual no aclaro la cantidad de parametros
def imprime_Texto(*text):
    print(text)

imprime_Texto("Hola", "Gisela", "Python", "Oh")
