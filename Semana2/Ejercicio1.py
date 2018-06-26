#!/usr/bin/Python
# -*- coding: utf-8 -*-

"""
Clase para devolver la tabla de multiplicar
"""

class Tabla():
#definimos el constructor
    def __init__(self, num):
        self.num = num
#definimos el print del objeto
    def __str__(self):
        return "Esta es la tabla del %s" %self.num
#función para imprimir la tabla
    def imprimeTabla(self):
        for i in range(1,11):
            print ('%s * %s = %s' %(self.num,i,self.num * i))
