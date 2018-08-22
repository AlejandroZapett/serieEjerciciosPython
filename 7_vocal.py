import argparse
def Vocal(letra):
	return letra+" es una vocal" if letra in ['a', 'e', 'i', 'o', 'u'] else "lo que ingresaste no es una vocal"

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--letra", help="Ingresa una letra")
args = parser.parse_args()
print(Vocal(args.letra))