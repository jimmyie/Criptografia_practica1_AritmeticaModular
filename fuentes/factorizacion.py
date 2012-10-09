#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Fichero: factorizacion.py
# Autor: César Aguilera
# Fecha: Abril 2012
#
from aritmetica_modular import test_primalidad_miller_rabin, algoritmo_rho_de_pollard, divisor_pequenio, algoritmo_de_strassen, metodo_factorizacion_fermat

def es_primo(n):
	if n <= 2:
		return True # Considero el 1 primo por cuestiones de programacion
	elif n&1 == 0: # Par
		return False
	else:
		return test_primalidad_miller_rabin(n,20)

def factoriza_en_primos(n):
	if es_primo(n) == False:
		# Encontrar un divisor mediante los diferentes algoritmos implementados (excepto fermat)
		for f in [divisor_pequenio, algoritmo_rho_de_pollard, algoritmo_de_strassen]:
				divisor = f(n)
				if divisor != None:
					break
		
		if divisor == n/divisor:
			a = factoriza_en_primos(divisor)
			b = a
		else: 
			a, b = factoriza_en_primos(n/divisor), factoriza_en_primos(divisor)

		a.extend(b) # Unificar en la misma lista la factorización de n/divisor y divisor
		return a
	else: 
		return [n]

print "\n##################################################"
print "####### Factorización de un número numeros #######"
print "############# como producto de primos ############"
print "##################################################\n"


print "1. Entrada: un número natural n." 
print "   Calcula una factorizacion del número n como producto de primos (Pollard + Strassen).\n"

print "2. Entrada: un número n, impar." 
print "   Calcula una factorización del número n utilizando el método de Fermat.\n"


opcion = long(raw_input("Introduce opción: "))
if opcion == 1:
	n = long(raw_input("Introduce n: "))
	print "Factores primos: ", sorted(factoriza_en_primos(n) )
elif opcion == 2:
	n = long(raw_input("Introduce n: "))
	print "Factores: ", metodo_factorizacion_fermat(n)
else:
	print "Opción inválida."