import string
# por simplicidad solo se permiten repeticiones de hasta 9 caracteres
def encode(input_file,output_file_name):
    file = open(input_file)                 
    data = file.read()   
    AUX = []
    repeat=1
    pre_character=data[0]
    for i in range(1,len(data)):
        if(data[i]==pre_character):
            repeat=repeat+1
        else:
            if(repeat==1):
                repeat=""
            AUX.append(str(repeat)+pre_character)
            repeat=1
            pre_character=data[i]
    if(repeat==1):
        repeat=""
    AUX.append(str(repeat)+data[i])
    AUX_str = "".join(AUX)
    output_file = open(output_file_name, "w")
    output_file.write(AUX_str)
    output_file.close
    file.close
    return(AUX_str)

def decode(input_file,output_file_name):
    file = open(input_file)                 
    data = file.read()   
    AUX_str=""
    len_data=len(data)
    for i in range(len_data):
        if(string.ascii_letters.find(str(data[i]))==-1):# si no encuentra cadena retorna -1, si esta retorna 0
            for m in range(1,int(data[i])):
                AUX_str=AUX_str+data[i+1]
        else:
            AUX_str=AUX_str+data[i]
    output_file = open(output_file_name, "w")
    output_file.write(AUX_str)
    file.close
    output_file.close
    return(AUX_str)



