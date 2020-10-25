import Generador_texto
from pathlib import Path
import RLE
import string
from tabulate import tabulate
from time import time
import Formulas_shannon


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
for i in range(1,31):
    #TEXTO GENERADO
    texto_generado=Generador_texto.generador_patrones(20,500)
    #Archivo de texto original
    output_file = open("Texto_generado"+str(i)+".txt", "w")
    output_file.write(texto_generado)
    output_file.close()
    #calculo de tamaño
    file = Path('Texto_generado'+str(i)+".txt") # or Path('./doc.txt')
    size1 = file.stat().st_size
    #Calculo de información y entropía
    datos=Formulas_shannon.Datos_shannon(size1,cdad_simbolos) #información,entropia
    #para la tabla
    archivo.append(str(i))
    tamaño_1.append(size1)
    informacion_1.append(datos[0])
    entropia_1.append(datos[1])

    #COMPRESION RLE
    start_time = time()
    texto_comprimido=RLE.encode("Texto_generado"+str(i)+".txt","Texto_generado_RLE"+str(i)+".txt")
    elapsed_time = time() - start_time
    file = Path('Texto_generado_RLE'+str(i)+".txt") # or Path('./doc.txt')
    size2 = file.stat().st_size
    #Calculo de información y entropía
    datos=Formulas_shannon.Datos_shannon(size2,cdad_simbolos) #información,entropia
    #para la tabla
    tamaño_2.append(size2)
    tiempo.append(elapsed_time)
    informacion_2.append(datos[0])
    entropia_2.append(datos[1])
    Tabla.append([archivo[i-1],tamaño_1[i-1],tamaño_2[i-1],tiempo[i-1],informacion_1[i-1],informacion_2[i-1],entropia_1[i-1],entropia_2[i-1]])

    #DESCOMPRESION RLE
    start_time = time()
    texto_descomprimido=RLE.decode("Texto_generado_RLE"+str(i)+".txt","Texto_generado_RLE_decode"+str(i)+".txt")
    elapsed_time = time() - start_time
    file = Path('Texto_generado_RLE_decode'+str(i)+".txt") # or Path('./doc.txt')
    size3 = file.stat().st_size
    datos=Formulas_shannon.Datos_shannon(size3,cdad_simbolos) #información,entropia
    #para comprobar descompresión
    #print("decode ",i,"|tamaño:",size3,"bits","|información:",datos[0],"|tiempo:",elapsed_time,"seg","|entropia:",datos[1])

print(tabulate(Tabla, headers='firstrow', tablefmt='fancy_grid'))

