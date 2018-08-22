import argparse

def extension(file):
	return "La extension del archivo es: "+file.split('.')[1]

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="Escribe el nombre de un archivo")
args = parser.parse_args()
print(extension(args.file))