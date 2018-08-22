import math
import argparse

def area(radio):
	return "El area es: "+str(math.pi*math.pow(radio,2))

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--radio", help="Ingresa un valor del radio")
args = parser.parse_args()
print(area(float(args.radio)))
