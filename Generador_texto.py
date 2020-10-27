import string
import random
def generador_cadena(n): #tamañodecadena
    str_cadena=""
    while(n>0):
        n=n-1
        str_cadena=str_cadena+random.choice(string.ascii_letters)
    return(str_cadena)
def generador_patrones(n,repeat): #tamañodelpatron,cantidad de veces que se repite    
    str_patron=generador_cadena(n)
    texto=""
    while(repeat>0):
        repeat=repeat-1
        texto=texto+str_patron
    return(texto)


#COMPRESION LZW
""" LZW.encode("Texto_generado.txt")
file = Path('Texto_generado.lzw') # or Path('./doc.txt')
size2 = file.stat().st_size
print("Archivo ",file," tiene tamaño de ",size2," bits") """
