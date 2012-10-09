#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Fichero: logaritmo.py
# Autor: César Aguilera
# Fecha: Abril 2012
#
from aritmetica_modular import logaritmo_discreto

print "\n##################################################"
print "############### Logaritmo Discreto ###############"
print "##################################################\n"

print "Calcula en Zp (p primo) el/los logaritmo/s de 'b' en base 'a'\n"

a = raw_input("Introduce base, a: ")
b = raw_input("Introduce exponente, b: ")
p = raw_input("Introduce módulo, p: ")

a, b, p = int(a), int(b), int(p)


print "Logaritmo discreto: ", logaritmo_discreto(a,b,p)