######   EL manejo de ERRORES   #####
#Este cápitulo trata sobre que hace el programa ante un evento no esperado que provoque un error, y asi evitar que mi programa muera o caiga
numberone, numbertwo=5, 1
numbertwo="1"

try:    #Pálabra reservada
    print(numberone+ numbertwo)
    #dentro del try va el código común
    print("No se ha producido un error")
except:  #Pálabra reservada
    print("Se ha producido un error")
    #Aca van los mensajes de aviso de error
else:
    print("La ejecución continúa correctamente")

