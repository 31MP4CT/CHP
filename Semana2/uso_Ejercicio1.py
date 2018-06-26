#!/usr/bin/Python
# -*- coding: utf-8 -*-

from Ejercicio1 import *

#preguntamos al usuario el número de la Tabla
num = int(input("Escoge la tabla de multiplicar que quieres obtener: "))
tabla = Tabla(num)
print tabla
#llamamos a la función para que nos imprima la tabla
tabla.imprimeTabla()
