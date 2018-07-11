from collections import Counter
import os

def falsowc(nombre_archivo):
#identifica los parrafos del archivo
#identifica la cantidad de palabras del archivo
#identifica los bytes del archivo

    def contarLineas(param):
        with open(param + '.txt', 'r') as mensaje:
            lineas = len(mensaje.readlines())
            return lineas  

    def contarPalabras(param):
        with open(param + '.txt', 'r') as mensaje:
            lineas = len(mensaje.read().split())
            return lineas  

    def contarBytes(param):
        with open(param + '.txt', 'r') as mensaje:
            lineas = os.stat(nombre_archivo + '.txt')
            return lineas.st_size  


    try:    #prueba que la variable x exista 
        archivo_ingresado = open(nombre_archivo + '.txt')

        lineas = contarLineas(nombre_archivo)
        lineas1 = contarPalabras(nombre_archivo)
        lineas2 = contarBytes(nombre_archivo)
        

        print('resumen de', nombre_archivo,':')
        print('cantidad de lineas:', lineas)
        print('cantidad de palabras:', lineas1)

        print('cantidad de bytes:', lineas2)
        
    except: #en caso de que no existe el archivo ejecuta el print (todavia NO FUNCA)
        print('El archivo', nombre_archivo,'no existe, por favor ingrese otro: ')
       
    
       
def llamado():
    x = input('ingrese el nombre del archivo que desee abrir: ')
    falsowc(x)

llamado()
