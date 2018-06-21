import numpy as np 


def frange(start, stop, step):
     i = start
     while i < stop:
         yield i
         i += step

def pasabanda(s, Ho, wo, Q):
	""" Retorna un vector con [pasbajo, pasabanda, pasaalto]"""
	a = (s/wo)**2
	b = s/(wo*Q)
	c = 1

	r = Ho / ( a + b + c )

	return np.absolute( r * b)


def calcular_parametros_pasabanda():
	print "frecuencia frecuencia_wo wo Q Ho valor_transferencia"
	frecuencias_entrada = [400, 600, 800]

	for frecuencia in frecuencias_entrada:
		w_entrada = 2 * np.pi * frecuencia 
		paso = 0.1 * frecuencia # el paso es el 10% del valor de la frecuencia de entrada

		for frecuencia_wo in frange(frecuencia/2, 1.5 * frecuencia + 1, paso): # frecuencia_wo = frecuencia_entrada/2 ... frecuencia* 3/2
			wo = 2 * np.pi * frecuencia_wo

			for Q in frange (0.1, 10, 0.1): # Q = 0.1, 0.2, 0.3, ..., 9.9

				for Ho in frange(0.1, 11, 0.1): # Ho = 0.1, 0.2, 0.3, ..., 10
					valor = pasabanda( w_entrada * 1j, Ho, wo, Q)

					if valor >= 0.95 and 10*(Q/wo) < 5*(10**(-3)) :
						print frecuencia, int(frecuencia_wo), wo, Q, Ho, valor
						break

calcular_parametros_pasabanda() 
