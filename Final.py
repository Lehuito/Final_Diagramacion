from collections import Counter
import os

def falsowc(nombre_archivo):
#identifica los parrafos del archivo
#identifica la cantidad de palabras del archivo
#identifica los bytes del archivo


    try:    #prueba que la variable x exista 
        archivo_ingresado = open(nombre_archivo + '.txt')
        
    except: #en caso de que no existe el archivo ejecuta el print (todavia NO FUNCA)
        print('El archivo ingresado no existe', nombre_archivo,'Por favor ingrese otro: ')
       

    with open(nombre_archivo + '.txt', 'r') as mensaje:
        
        print('resumen de', nombre_archivo,':')

        lineas = len(mensaje.readlines())

        mensaje.seek(0)

        contador = len(mensaje.read().split())

        mensaje.seek(0)

        aux = os.stat(nombre_archivo + '.txt')

        cuenta_bytes = aux.st_size


        print('cantidad de lineas:', lineas)
    
        print('cantidad de palabras:', contador)

        print('cantidad de bytes:', cuenta_bytes)
       
def llamado():
    x = input('ingrese el nombre del archivo que desee abrir: ')
    falsowc(x)

llamado()
