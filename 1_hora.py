import datetime
def hora():
	return "El dia es: "+str(datetime.datetime.now().day)+" y la hora es: "+str(datetime.datetime.now().hour)

print(hora())