import argparse

# Creo el parser
parser = argparse.ArgumentParser(description='Saluda al usuario.')

# Agrego un argumento -n o --nombre
parser.add_argument('-n', '--nombre', type=str, required=True, help='Nombre del usuario')

# Parseo los argumentos
args = parser.parse_args()

# Uso el argumento
print(f'Hola, {args.nombre}!')
