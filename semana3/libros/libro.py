#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .atributos import *
############################
#       Clase Libro        #
############################

class Libro():
    #Creamos los atributos(objeto)
    #titulo = Titulo(None)
    #autor = Autor(None)
    #editorial = Editorial(None)
    #paginas_totales = Paginas_Totales(None)
    #paginas_leidas = Paginas_Leidas(None)

    #constructor
    def __init__(self,titulo, autor,
                editorial, paginas_totales, paginas_leidas):
                self.titulo =  titulo
                self.autor = autor
                self.editorial = editorial
                self.paginas_totales = paginas_totales
                self.paginas_leidas = paginas_leidas
    #escribimos el print
    def __str__(self):
        return ('El libro "%s" de %s (editorial %s) tiene %s páginas y llevas leídas %s' %(self.titulo, self.autor,
                    self.editorial, self.paginas_totales, self.paginas_leidas))

    #método para actualizar las páginas leídas
    def setPaginas_leidas(self,paginas):
        self.paginas_leidas = paginas
