import time
import RPi.GPIO as GPIO #Libreria GPIO
GPIO.setmode(GPIO.BCM) #Configuracion de puertos
GPIO.setwarnings(False)

entradas=(2,3,4,17,27,22,10,9)#vector de pines de entrada
salidas=(14,15,18,23,24,25)#Vector de pines de salida

#inicilizacion de entradas
for i in entradas:
	GPIO.setup(i, GPIO.IN)
#Asignacion de nombre a entradas
TAA=2
TAB=3
TBA=4
TBB=17
TCA=27
TCM=22
TCB=10
START=9

#inicializacion de salidas
for i in salidas:
	GPIO.setup(i,GPIO.OUT)
#Asignacion de nombre a salidas
BA=14
BB=15
VA=18
VB=23
AG=24
AL=25

#Variables de Control
band = True

while True:
#Bloque de desicion para el inicio del proceso.
	if (GPIO.input(START) == 1 and band == True):
		print("proceso iniciado")
		#Ciclo de llenado del tanque C.
		while((TAA == 1 or TBA == 1) and TCB == 0):

			#Bloque de desicion, si el sensor de bajo nivel del tanque A esta activo, entonces llena tanq. C por 30 sec.
			if (GPIO.input(TAB) == 1):
				GPIO.output(BA,0)
				time.sleep(30)
				if (TBB == 1):
					GPIO.output(BA,1)


			#Bloque de desicion, si el sensor de bajo nivel del tanque B esta activo, entonces llena tanq. C por 30 sec.
			if(GPIO.input(TBB) == 1):
				GPIO.output(BB,0)
				time.sleep(30)
				if (TBA == 1):
					GPIO.output(BB,1)

		#Ciclo Vaciado del tanque C.
		c = 0
		while(GPIO.input(TCB) == 1 and c < 3600):

			GPIO.output(AG,0)
			GPIO.output(VA,0)
			time.sleep(30)
			c = c + 30
			GPIO.output(AG,1)
			GPIO.output(VA,1)
			GPIO.output(VB,0)
			time.sleep(30)
			c = c + 30
			GPIO.output(VB,1)

		if c == 3600:
			GPIO.output(AL,0)
			time.sleep(10)
			GPIO.output(AL,1)

		band = False

