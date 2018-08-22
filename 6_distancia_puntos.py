import argparse

def distancia_puntos(num):
	return "La distancia entre los dos puntos es: "+str(abs(int(num)-17))

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--num", help="Ingresa un numero")
args = parser.parse_args()
print(distancia_puntos(args.num))