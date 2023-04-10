###Condicionales#####

my_condition= True

if my_condition:
    print("Se imprime el primer condicional")

my_condition=5*2

if my_condition==10:
    print("Se ejecuta el segundo condicional")

if my_condition>10:
    print("Se ejecuta el tercer if")
else:
    print("Utilizo el else del tercer condicionador")

if my_condition >10 and my_condition<20:
    print("Mi condicion es mayor a 10 y menor a 20")
elif my_condition==1:
    print("Mi condicion es igual a 1")
else:
    print("Es menor a 10")

my_string=""

if not my_string:
    print("Mi cadena esta vacia")

if my_string==("Mi cadena de textoooo"):
    print("Estas cadenas son iguales")
    

print("Continua la ejecucion")
