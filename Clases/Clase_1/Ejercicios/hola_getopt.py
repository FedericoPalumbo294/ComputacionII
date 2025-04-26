import sys
import getopt

# Leo los argumentos de la terminal (menos el nombre del script)
argumentos = sys.argv[1:]

# Defino las opciones esperadas: -n <nombre>
opciones, resto = getopt.getopt(argumentos, "n:")

# Recorro las opciones que encontró
for opcion, valor in opciones:
    if opcion == '-n':
        print(f'Hola, {valor}!')
