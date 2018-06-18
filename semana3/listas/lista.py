#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import libros
from libros.comic import *
######################
#      Clase Lista   #
######################
"""
Esta clase está creada con la intención de instanciar una lista global para almacenar libros y comics,
se monta aparte del main, para hacerla privada y así poder experimentar un poco más con la orientación a objetos.
Todos los métodos necesarios para manejar la lista están definidos más abajo, menos un método para eliminar libros,
no obstante sería tan sencillo como usar el método find() y la función remove(x) propia de las listas.
"""
class Lista():
    #constructor
    def __init__(self):

        self.lista = []

    #Permite añadir libros o comics a la Lista
    def addtoLista(self,item):
        self.lista.append(item)
        return 'El elemento %s ha sido correctamente introducido'%(item.titulo)

    #Metodo añadido para imprimir la lista de libros/comics
    def printLista(self):
        for i in range(len(self.lista)):
            description = print(self.lista[i])
            if description is not None:
                print(description)

    #Permite encontrar un libro/comic por su titulo y devuelve el objeto
    def find(self,nombre):
        match = None
        aux = True
        while(aux):
            for i in self.lista:
                if (self.lista[self.lista.index(i)].titulo.lower()== nombre.lower()):
                    print ("¿Es este tu libro/comic? ")
                    print (i)
                    if(int(input("1.Sí 2.No "))==1):
                        match = self.lista[self.lista.index(i)]
                        aux = False
        return match

    #Devuelve el número de elementos de la lista (no se utiliza)
    def numberElements(self):
        return len(self.lista)

    #Permite actualizar el número de páginas leídas, hay que parser el libro/comic. Devuelve False
    def updatePages(self,lectura):
        #Creamos un bucle para asegurarnos de que el usuario introduce el número de páginas correcto
        aux = True
        while(aux):
            leidas = int(input("¿Cuántas páginas has leído?: "))
            if((leidas+lectura.paginas_leidas)<=lectura.paginas_totales):
                if ((leidas+lectura.paginas_leidas)==lectura.paginas_totales):
                    print ("Enhorabuena, has terminado la lectura al 100%")
                else:
                    print ('Bien hecho aún te quedan %s páginas' %(lectura.paginas_totales-(leidas+lectura.paginas_leidas)))
                #Actualizamos las páginas leídas en el elemento real almacenado en 'lista'
                lectura.setPaginas_leidas(leidas+lectura.paginas_leidas)
                indice = self.lista.index(lectura)
                self.lista[indice] = lectura
                aux = False
            else:
                print ("Por favor introduce un número correcto de paǵinas")

        return False
