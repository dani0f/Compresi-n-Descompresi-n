from huffman import HuffmanCoding
import sys
from time import time
from pathlib import Path

path = "Texto_generado_patron.txt"

h = HuffmanCoding(path)

start_time = time()
output_path = h.compress()
elapsed_time = time() - start_time

print("Compressed file path: " + output_path)

decom_path = h.decompress(output_path)

print("Decompressed file path: " + decom_path)

file = Path("Texto_generado_patron.bin") # or Path('./doc.txt')
size = file.stat().st_size
print("tiempo: ",elapsed_time)
print("tamaño dsp de compresión",size)