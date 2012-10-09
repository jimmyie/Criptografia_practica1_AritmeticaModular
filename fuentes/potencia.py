#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Fichero: potencia.py
# Autor: César Aguilera
# Fecha: Abril 2012
#
from aritmetica_modular import potencia_modular

print "\n##################################################"
print "################ Potencia Modular ################"
print "##################################################\n"

print "Calcula en Zp la potencia 'a' elevado a 'b'\n"

a = raw_input("Introduce base, a: ")
b = raw_input("Introduce exponente, b: ")
p = raw_input("Introduce módulo, p :")

a, b, p = int(a), int(b), int(p)


print "Potencia modular: ", potencia_modular(a,b,p)