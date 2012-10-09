#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Fichero: primalidad.py
# Autor: César Aguilera
# Fecha: Abril 2012
#
import random
import math
from aritmetica_modular import test_primalidad_miller_rabin

def resultado_test_primalidad(p, n):
	if test_primalidad_miller_rabin(p, n):
		return str(p) + " es probable primo, probabilidad " + str( 1.0 - 1./(4.**n))
	else: 
		return str(p) + " no es primo"

print "\n##################################################"
print "############### Test de Primalidad ###############"
print "##################################################\n"

print "1. Entrada: dos número naturales: p y n, p impar." 
print "   Comprobar si el número p pasa el test n veces.\n"

print "2. Entrada: dos números naturales: c y n."
print "   Generar un número impar de p de c cifras."
print "   Comprobar si el número p pasa el test n veces.\n"

print "3. Entrada: un número impar natural p y un número real h en (0,1) "
print "   Comprobar si el número p pasa el test con probabilidad h\n"

print "4. Entrada: un número natural n"
print "   Generar un número primo de n cifras\n"



opcion = int(raw_input("Introduce opción: "))
print 

n, p  = 0, 0 

if opcion == 1:
	p = int(raw_input("Introduce p: "))
	n = int(raw_input("Introduce n: "))
elif opcion == 2:
	c = int(raw_input("Introduce c: "))
	n = int(raw_input("Introduce n: "))
	p = 2
	while(p&1 != 1):
		p = random.randint(10**(c-1),10**c)
elif opcion == 3:
	p = int(raw_input("Introduce p: "))
	h = float(raw_input("Introduce h: ")) 
	n = int(math.ceil(math.log(1./(1.-h),4)))
	print n
elif opcion == 4:
	n = int(raw_input("Introduce n: "))
	primo = False
	while primo == False: 
		p = random.randint(10**(n-1), 10**n )
		if p&1 == 0:
			continue # evito números pares
		if test_primalidad_miller_rabin(p,10): # 0.999999 probabilidad de ser primo
			primo = True
	n = 10
else:
	print "Opción no válida"
	exit()

print "\n", resultado_test_primalidad(p,n)