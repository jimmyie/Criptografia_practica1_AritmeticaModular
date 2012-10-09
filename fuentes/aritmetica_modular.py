#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Fichero: aritmetica_modular.py
# Autor: César Aguilera
# Fecha: Abril 2012
#
from math import sqrt, ceil
from fractions import gcd
import random
import decimal

def potencia_modular(a, b, p):
	"""	Descripción: Calcula en Zp la potencia modular de a elevado a b.
	Parámetro a: base.
	Parámetro b: exponente.
	Parámetro p: módulo que se aplica.
	Precondiciones: a, b y p deben ser números enteros positivos.
	Devuelve: a elevado a b módulo p."""
	res = 1 
	base = a 
	exp = b
	while exp != 0 :
		if exp & 1: 
			res = (res * base) % p
		exp = exp >> 1
		base = (base * base) % p
	
	return res


def logaritmo_discreto(a, b, p):
	"""	Descripción: Calcula en Zp el (los) logaritmo(s) de b en base a.
	Precondiciones: a, b y p deben ser números enteros positivos, además p debe ser primo.
	Parámetro a: base.
	Parámetro b: exponente.
	Parámetro p: módulo que se aplica.
	Devuelve: Una lista con los logaritmos discretos de b en base a módulo p. Si no 
	existe el logaritmo discreto devuelve valor nulo."""
	
	s = long(ceil(sqrt(p - 1))) # s = entero inmediatamente superior a la raíz de p-1
	vr = [] # elemento r-ésimo de vr es (a^r)*b
	vr.append(b) # primer elemento de vr es b, es decir: vr[0] = b (para el caso r = 0)
	
	for r in range(1, s): # desde r = 1 hasta r = s-1
		vr.append((vr[r - 1] * a) % p) # elemento r-ésimo de vr es el producto (en Zp) del anterior
		# por a, es decir: vr[r] = vr[r-1]*a mód p
		
	res = [] # vector de resultados (logaritmos)
	
	for t in range(1, s + 1): # desde t = 1 hasta t = s
		aux = potencia_modular(a, t * s, p) # aux es a^(t*s) en Zp
		try: # si a^(t*s) está en vr
			res.append(t * s - vr.index(aux)) # añadir a res el valor t*s-r
		except ValueError:
			pass
		
	if res == []:
		res = None # res es nulo si no existe el logaritmo en base a de b mód p
	
	return res


def test_primalidad_miller_rabin(p, n):
	"""	Descripción: Determina si un número es primo mediante el 
		test de primalidad probabilístico de Miller-Rabin.
	Precondiciones: p y n deben ser números enteros positivos, además p debe ser impar.
	Parámetro p: número a pasar el test de primalidad.
	Parámetro n: número máximo de rondas que se aplica el test de primalidad a p.
	Devuelve: False si p no es primo. True si p es probable primo."""
	
	if p & 1 == 0:
		return False

	if p < 6: # Esta implementacion de Miller-Rabin funciona a partir de p = 5
		return p in [2,3,5]
	
	else:
		primo = True	
		u = 0
		s = p - 1
		while(s & 1 == 0): # Expresar p-1 como (2^u)*s, s impar
			u = u + 1
			s = s / 2
			
		for rondas in range(n):
			a = random.randint(2, p - 2) # a al azar entre 2 y p-2 (ambos inclusive)
			a = potencia_modular(a, s, p) # a = a^s
			if a == 1 or a == (p - 1): # si a = 1 ó a = p-1
				primo = True  # p probable primo
			else:
				i = 1
				while i != u : #desde i = 1 hasta u-1
					a = (a * a) % p	
					if a == (p - 1):
						primo = True # p es probable primo
						break
					elif a == 1:
						primo = False # p no es primo
						break
					
					i = i + 1
				
				if i == u:
					primo = False # p no es primo
				
			if primo == False:
				break # Si ya se ha determinado que no es primo, parar el bucle de rondas

		return primo




def metodo_factorizacion_fermat(n):
	"""	Descripción: Determina la factorización de un número n como producto de una suma 
	por una diferencia, mediante el método de factorización de Fermat.
	Precondiciones: n debe ser un número entero positivo impar no primo.
	Parámetro n: número a factorizar.
	Devuelve: Representación de n como como producto de una suma 
	por una diferencia (diferencia de dos cuadrados)."""
	
	x = long(ceil(sqrt(n))) # x = entero inmediatamente superior a la raíz de n
	while True:
		y = x**2 - n
		
		if y < 0:
			return __metodo_factorizacion_fermat_preciso__(n)
		
		ry = sqrt(y)
		if ry.is_integer(): # si la raiz de y no tiene parte decimal, y es cuadrado perfecto
			a = long(x+ry)
			b = long(x-ry)
			
			if a*b != n:
				return __metodo_factorizacion_fermat_preciso__(n)
			
			return [a,b]

		x = x+1
			
def __metodo_factorizacion_fermat_preciso__(n):
	decimal.getcontext().prec = 50
	n = decimal.Decimal(n)
	x = n.sqrt().to_integral_value(rounding=decimal.ROUND_CEILING)
	while True:
		y = x**2 - n
		ry = y.sqrt().to_integral_value(rounding=decimal.ROUND_FLOOR)
		if (ry*ry) == y:
			a = long(x+ry)
			b = long(x-ry)
			return [a,b]

		x = x+1


def algoritmo_rho_de_pollard(n):
	"""	Descripción: Calcula un divisor de n mediante el algoritmo Rho de Pollard.
	Precondiciones: n debe ser un número entero positivo.
	Parámetro n: número a factorizar.
	Devuelve: Divisor de n en caso de encontrarlo. Valor nulo en otro caso."""
	f = lambda x: (x**2+1)%n
	a = random.randint(1, n - 1) # a al azar entre 1 y n-1 (ambos inclusive)
	x = f(a)
	y = f(x)
	i = 1
	I = 1000 # Número máximo de iteraciones
	
	while i != I:
		d = gcd(y-x, n)
		if d == 1:
			i = i + 1
			x = f(x)
			y = f(f(y))
		else:
			return d
	
	return None


def algoritmo_de_strassen(n):
	"""	Descripción: Calcula un divisor de n mediante el algoritmo de Strassen.
	Precondiciones: n debe ser un número entero positivo.
	Parámetro n: número a factorizar.
	Devuelve: Divisor de n en caso de encontrarlo. Valor nulo en otro caso."""
	b = long(ceil(sqrt(n)))
	c = long(ceil(sqrt(b - 1))) # c = entero inmediatamente superior a la raíz de b-1
	p = lambda x: reduce(lambda u,v: u*v , [(k+x)%n for k in range(1,c+1)]) % n # p(x)
	for i in range(c):
		g = p(c*i)
		d = gcd(g, n)
		if d != 1:
			break

	if d == 1:
		d = None

	return d

def divisor_pequenio(n):
	"""	Descripción: Calcula un divisor primo (menor que 6) de n
	Parámetro n: número a factorizar.
	Devuelve: Divisor de n en caso de encontrarlo. Valor nulo en otro caso."""
	if n == 1:
		return 1L
	elif n&1 == 0:
		return 2L
	elif n%3 == 0:
		return 3L
	elif n%5 == 0:
		return 5L

	return None