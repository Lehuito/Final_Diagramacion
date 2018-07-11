import os

def falsowc(nombre_archivo):
#identifica los parrafos del archivo.
#identifica la cantidad de palabras del archivo.
#identifica los bytes del archivo.
#no hace falta que se agregue la extensión en el nombre del archivo.

    def contarLineas(param): #cuenta las lineas del archivo ingresado.
        with open(param + '.txt', 'r') as mensaje:
            lineas = len(mensaje.readlines())
            return lineas  

    def contarPalabras(param): #cuenta las palabras archivo ingresado
        with open(param + '.txt', 'r') as totalPalabras:
            palabras = len(totalPalabras.read().split())
            return palabras  

    def contarBytes(param): #calcula la cantidad de bytes que pesa el archivo.
        open(param + '.txt', 'r')
        totalByte = os.stat(nombre_archivo + '.txt')
        return totalByte.st_size

    def contarLarga(param):
        with open(param + '.txt', 'r') as larguita:
                todas = larguita.readlines()
                masLarga = 0
                for lineas in todas:
                    otra = len(lineas)
                    if otra > masLarga:
                        masLarga = otra

                return masLarga           


    try:    #prueba que el archivo ingresado exista, si existe lo abre y sigue ejecutando el programa 
        archivo_ingresado = open(nombre_archivo + '.txt')

        lineas = contarLineas(nombre_archivo)
        palabras = contarPalabras(nombre_archivo)
        totalByte = contarBytes(nombre_archivo)
        lineaLarga = contarLarga(nombre_archivo)

        #importante printear las siguientes lineas ya que el return de cada funcion creada no nos muestra lo solicitado.
        print('resumen de', nombre_archivo,':')
        print('cantidad de lineas:', lineas)
        print('cantidad de palabras:', palabras)
        print('cantidad de bytes:', totalByte)
        print('la linea MAS LARGA es:', lineaLarga)

    except: #en caso de que no exista el archivo ingresado ejecuta el print de abajo.
        print('El archivo', nombre_archivo,'no existe, por favor ingrese otro: ')
        
    
       
def llamado(): #solicita una entrada al usuario y se le agrega a la funcion falsowc para que luego este ejecute el código.
    x = input('ingrese el nombre del archivo que desee analizar: ')
    falsowc(x)

llamado()
