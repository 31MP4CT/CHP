#!/usr/bin/env python3
# -*- coding: utf-8

from .libro import *

############################
#     Clase Comic          #
###########################
#Hereda de la clase Libro
class Comic(Libro):
    dibujante = Dibujante(None)
    #constructor
    def __init__(self, titulo, guionista, dibujante, editorial,
                paginas_totales, paginas_leidas):
                Libro.__init__(self,titulo,guionista,editorial,paginas_totales,paginas_leidas)
                self.dibujante = dibujante
    #escribimos el print
    def __str__(self):
        return ('El Comic "%s" (editorial %s)  escrito por %s y dibujado por %s, tiene %s páginas y llevas leídas %s' %(self.titulo, self.editorial,
                    self.autor, self.dibujante, self.paginas_totales, self.paginas_leidas))
