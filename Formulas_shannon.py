import math
#información, probabilidad y entropia de Shannon 
def Info_shannon(cdad_simbolos):
    return(math.log2(cdad_simbolos))
def Probabilidad_shannon(cdad_simbolos):
    return(1/cdad_simbolos)
def Datos_shannon(largo,cdad_simbolos):
    sum=0
    info=0
    for i in range(largo):
        info_shannon=Info_shannon(cdad_simbolos)
        info=info+info_shannon
        sum=sum+(Probabilidad_shannon(cdad_simbolos) * info_shannon)
    return([info,sum])