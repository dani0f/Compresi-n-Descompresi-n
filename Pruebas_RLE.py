import Generador_texto
from pathlib import Path
import RLE
import string
import math
from tabulate import tabulate
from time import time


def Info_shannon(frecuencia,largo):
    return(math.log2(largo/frecuencia))
def Probabilidad_shannon(frecuencia,largo):
    return(frecuencia/largo)
def Datos_shannon(frecuencias,largo):
    sum=0
    info=0
    for i in range(len(frecuencias)):
        info_shannon=Info_shannon(frecuencias[i],largo)
        info=info+info_shannon
        sum=sum+(Probabilidad_shannon(frecuencias[i],largo) * info_shannon)
    return([info,sum])

def Frecuencias(data):
    list_letras= []
    list_cdad= []
    for i in range(len(data)):
        cantidad=list_letras.count(data[i])
        if(cantidad==0):
            frecuencia=data.count(data[i])
            list_letras.append(data[i])
            list_cdad.append(frecuencia)
    return(list_cdad)

""" def Informacion(cdad_simbolos,largo_mensaje):  CALCULO DE DATOS MODO 2 SIN FRECUENCIAS
    cdad_simbolos=pow(cdad_simbolos,largo_mensaje)
    informacion=math.log2(cdad_simbolos) 
    return(informacion)
def Probabilidad_error(cdad_simbolos,largo_mensaje):
    pe=pow((1/cdad_simbolos),largo_mensaje)
    return(pe)
def Entropia(pe,informacion,m):
    entropia=0
    #m son los posibles caracteres en este caso son 52 y el largo del mensaje es de 40
    for i in range(1,m):
        entropia=entropia+pe*informacion
    return(entropia) """

#MAIN
#SIMBOLOS POSIBLES
cdad_simbolos=len(string.ascii_letters)
#Datos para generar la tabla
archivo = []
tamaño_1 = []
informacion_1 =[]
tamaño_2 = []
informacion_2 =[]
tiempo = []
entropia_1 = []
entropia_2 = []
Tabla = []
Tabla.append(['Archivo',"Original(bits)","Comprimido(bits)","Tiempo(seg)","I original","I encode","H original","H encode"])
p=0
for i in range(1,31):
    #TEXTO GENERADO
    texto_generado=Generador_texto.generador_cadena(1000)
    #Archivo de texto original
    output_file = open("Texto_generado"+str(i)+".txt", "w")
    output_file.write(texto_generado)
    output_file.close()
    #calculo de tamaño
    file = Path('Texto_generado'+str(i)+".txt") # or Path('./doc.txt')
    size1 = file.stat().st_size
    #Calculo de información y entropia
    list_frecuencias=Frecuencias(texto_generado)
    datos=Datos_shannon(list_frecuencias,size1) #información,entropia
    #para la tabla
    archivo.append(str(i))
    tamaño_1.append(size1)
    informacion_1.append(datos[0])
    entropia_1.append(datos[1])

    #print("original ",i,"|tamaño:",size1,"bits","|información:",datos[0],"|entropia:",datos[1])

    #COMPRESION RLE
    start_time = time()
    texto_comprimido=RLE.encode("Texto_generado"+str(i)+".txt","Texto_generado_RLE"+str(i)+".txt")
    elapsed_time = time() - start_time
    file = Path('Texto_generado_RLE'+str(i)+".txt") # or Path('./doc.txt')
    size2 = file.stat().st_size
    #Calculo de información y entropia
    list_frecuencias=Frecuencias(texto_comprimido)
    datos=Datos_shannon(list_frecuencias,size2) #información,entropia
    #para la tabla
    tamaño_2.append(size2)
    tiempo.append(elapsed_time)
    informacion_2.append(datos[0])
    entropia_2.append(datos[1])
    Tabla.append([archivo[i-1],tamaño_1[i-1],tamaño_2[i-1],tiempo[i-1],informacion_1[i-1],informacion_2[i-1],entropia_1[i-1],entropia_2[i-1]])

    #print("encode ",i,"|tamaño:",size2,"bits","|información:",datos[0],"|tiempo:",elapsed_time,"seg","|entropia:",datos[1])

    #DESCOMPRESION RLE
    start_time = time()
    texto_descomprimido=RLE.decode("Texto_generado_RLE"+str(i)+".txt","Texto_generado_RLE_decode"+str(i)+".txt")
    elapsed_time = time() - start_time
    file = Path('Texto_generado_RLE_decode'+str(i)+".txt") # or Path('./doc.txt')
    size3 = file.stat().st_size
    list_frecuencias=Frecuencias(texto_comprimido)
    datos=Datos_shannon(list_frecuencias,size3) #información,entropia
    #para la tabla
    #print("decode ",i,"|tamaño:",size3,"bits","|información:",datos[0],"|tiempo:",elapsed_time,"seg","|entropia:",datos[1])

print(tabulate(Tabla, headers='firstrow', tablefmt='fancy_grid'))

