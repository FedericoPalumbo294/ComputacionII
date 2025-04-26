# 📋 Este programa copia el contenido de un archivo de texto a otro.
# El usuario debe pasar el archivo de entrada con -i y el de salida con -o por terminal.
# Si el archivo de entrada no existe, se muestra un mensaje de error.

import argparse

# Creo el parser
parser = argparse.ArgumentParser(description='Copiar contenido de un archivo de texto a otro.')

# Agrego un argumento -i o --input
parser.add_argument('-i', '--input', type=str, required=True, help='Archivo de entrada (txt)')

# Agrego un argumento -o o --output
parser.add_argument('-o', '--output', type=str, required=True, help='Archivo de salida (txt)')

# Parseo los argumentos
args = parser.parse_args()

# Intento abrir el archivo de entrada y copiar su contenido
try:
    with open(args.input, 'r') as archivo_entrada:
        contenido = archivo_entrada.read()

    with open(args.output, 'w') as archivo_salida:
        archivo_salida.write(contenido)

    print(f" Se copió el contenido de {args.input} a {args.output}.")
except FileNotFoundError:
    print(f" Error: el archivo '{args.input}' no existe.")
