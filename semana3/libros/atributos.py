#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
En esta clase se definiran las clases de los atributos
con sus descriptores correspondientes

"""
#############################
#   Clase (atributo) Titulo #
#############################

class Titulo():
    def __init__(self, titulo):
        self.titulo = titulo

    def __get__(self, clase, object):
        return str(self.titulo)

    def __set__(self, object, value):
        try:
            self.titulo = str(value)
        except ValueError:
            print("Introduzca una cadena de texto")

    def __del__(self, object):
        del self.titulo

#############################
#   Clase (atributo) Autor #
#############################

class Autor():
    def __init__(self, autor):
        self.autor = autor

    def __get__(self, clase, object):
        return self.autor

    def __set__(self, object, value):
        try:
            self.autor = str(value)
        except ValueError:
            print("Introduzca una cadena de texto")

    def __del__(self, object):
        del self.autor

#############################
#   Clase (atributo) Editorial #
#############################

class Editorial():
    def __init__(self, editorial):
        self.editorial = editorial

    def __get__(self, clase, object):
        return self.editorial

    def __set__(self, object, value):
        try:
            self.editorial = str(value)
        except ValueError:
            print("Introduzca una cadena de texto")

    def __del__(self, object):
        del self.editorial

######################################
#   Clase (atributo) Paginas_Totales #
######################################

class Paginas_Totales():
    def __init__(self, paginas_totales):
        self.paginas_totales = paginas_totales

    def __get__(self, clase, object):
        return self.paginas_totales

    def __set__(self, object, value):
        try:
            self.paginas_totales = int(value)
        except ValueError:
            print("Introduzca un número")
            self.paginas_totales = 0
    def __del__(self, object):
        del self.paginas_totales

######################################
#   Clase (atributo) Paginas_Leidas #
######################################

class Paginas_Leidas():
    def __init__(self, paginas_leidas):
        self.paginas_leidas = paginas_leidas

    def __get__(self, clase, object):
        return self.paginas_leidas

    def __set__(self, object, value):
        try:
            self.paginas_leidas = int(value)
        except ValueError:
            print("Introduzca un número")
            self.paginas_leidas = 0
    def __del__(self, object):
        del self.paginas_leidas

################################
#   Clase (atributo) Dibujante #
################################

#Atributo especifico de la clase Comic

class Dibujante():
    def __init__(self, dibujante):
        self.dibujante = dibujante

    def __get__(self, clase, object):
        return self.dibujante

    def __set__(self, object, value):
        try:
            self.dibujante = str(value)
        except ValueError:
            print("Introduzca una cadena de texto")

    def __del__(self, object):
        del self.dibujante
