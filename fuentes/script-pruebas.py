#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Fichero: script-pruebas.py
# Autor: César Aguilera
# Fecha: Abril 2012
#

from timeit import Timer
from functools import partial
from aritmetica_modular import potencia_modular, logaritmo_discreto
from random import randint

def get_execution_time_in_seconds(function, args=(), kwargs ={}, numberOfExecTime=1):
    return round(Timer(partial(function, *args, **kwargs)).timeit(numberOfExecTime), 8) # Precision tiempo 8 decimales


mismo_num_cifras = lambda c: randint(10**(len(str(c))-1), 10**( len (str(c) ))  )

P = [52691, 843587, 4872961, 29873761, 537891269, 1547598739, 82376849239, 576382750891, 5134857695843]

A = [mismo_num_cifras(i) for i in P]
B = [mismo_num_cifras(i) for i in P]


print "%s\t%s\t%s\t%s\t%s\t%s\t%s" % ("p", "a", "b", "c", "d", "tc", "td")
for i in range(len(P)):
	a, b, p = A[i], B[i], P[i]
	c = potencia_modular(a, b, p)
	d = logaritmo_discreto(a,c,p)
	tc = get_execution_time_in_seconds(potencia_modular, (a,b,p))
	td = get_execution_time_in_seconds(logaritmo_discreto, (a,c,p))
	print "%s\t%s\t%s\t%s\t%s\t%s\t%s" % (p, a, b, c, d, tc, td)