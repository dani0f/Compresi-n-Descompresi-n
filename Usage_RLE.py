#USAGE
# For encode: python RLE.py encode Codigo.txt RLE_encode.txt
# For decode: python RLE.py decode RLE_encode.txt RLE_decode.txt
import RLE
import sys
print("argumentos pasados", sys.argv)
action=sys.argv[1]#encode o decode
input_file=sys.argv[2]#input file
output_file=sys.argv[3]#output file
if(action == "encode"):
    aux=RLE.encode(input_file,output_file)
if(action == "decode"):
    aux=RLE.decode(input_file,output_file) 