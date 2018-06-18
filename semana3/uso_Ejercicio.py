#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import libros,listas.lista
from libros.libro import *
from libros.comic import *
from listas.lista import *

#La Clase Comic ya importa Atributos y Libro


####################
# Uso Ejercicio #
#####################

#instanciamos una lista a través del objeto Lista y usamos los métodos para añadir los libros/comics creados anteriormente
my_lista=Lista()

#Creamos el objeto my_libro (en forma de lista para usar más adelante)
my_libro = []
my_libro.append(Libro("Hacking con Python","Daniel Echeverri Montoya","0xW0RD",287,0))
#Imprimimos por pantalla la información para comprobar que está 0k
#print (my_libro[0])
#Modificamos las páginas leídas
my_libro[0].setPaginas_leidas(10)
#Comprobamos que se han modificado correctamente
#print (my_libro[0])

my_lista.addtoLista(my_libro[0])

#Creamos el objeto my_comic (en forma de lista para usar más adelante)
my_comic= []
my_comic.append(Comic("Animal Man", "Jeff Lemire", "Andrea Sorrentino","DC",93,0))
#Imprimimos por pantalla para ver que está correcto
#print (my_comic[0])
#Modificamos las páginas leídas
my_comic[0].setPaginas_leidas(30)
#Comprobamos que se han modificado 0k
#print (my_comic[0])

my_lista.addtoLista(my_comic[0])

#####################################
#  Uso de la clase Lista y añadidos #
#####################################
print (my_lista.printLista())
print('\n\n\n')
bucle = True
#Hacemos un bucle para no tener que salir del programa todo el rato
while(bucle):
    print ("Bienvenido a la librería de f.society.")
    print ("Aquí encontrarás todo tipo de libros y comics rescatados de la red")
    print ("¿Qué operación desea realizar?")
    #Obtenemos la opción del usuario
    operacion = int(input("1.Introducir Libros/Comics al sistema.\n2.Leer algún libro/comic del sistema.\n3.Salir del programa.\n"))

    if(operacion == 1):
        print ("¿Qué vas a introducir, Libro o Comic?")
        if(int(input("1.Libro 2.Comic: "))==1):
            #Instanciamos un Libro de forma dinámica añadiendolo a la lista my_libro y obteniendo los parámetros del usuario
            my_libro.append(Libro(str(input("¿Cuál es el título? ")),str(input("¿Quién es el autor? ")),str(input("¿Editorial? ")),int(input("¿De cuántas páginas es el libro? ")),0))
            #usando los métodos definidos en la clase Lista, añadimos el libro a la lista parseando el libro en sí mismo
            #para ello usamos la lista my_libro y el libro que acabamos de añadir se encontraŕa en length -1 (si hay 4 libros, la posición 3 de la lista)
            print (my_lista.addtoLista(my_libro[len(my_libro)-1]))
        else:
            #Lo mismo que en los libros, pero si se trata de un objeto comic
            my_comic.append(Comic(str(input("¿Cuál es el título? ")),str(input("¿Quién el el guionista? ")),str(input("¿Y el dibujante? ")),str(input("¿Editorial? ")),int(input("¿De cuántas páginas es el cómic? ")),0))
            print (my_lista.addtoLista(my_comic[len(my_comic)-1]))

        print('\nMuchas gracias por tu aportación, actualmente contamos con %s elementos en nuestra librería: %s libros y %s comics'%(my_lista.numberElements(),len(my_libro),len(my_comic)))

    elif(operacion == 2):
        #Obtenemos el objeto libro/comic de la lista global creada en my_lista a través del método definido en su clase, ver método find del archivo Ejercicio2y3.py
        lectura = my_lista.find(str(input("¿Cuál es el título de tu libro/comic? ")))
        print ('Disfruta tu lectura: %s. No tengas prisa...' %lectura)
        #Creamos la variable booleana reading para montar un bucle de lectura, se usará más adelante
        reading = True
        while(reading):
            print (".......................................")
            print ("..........Tomate tu tiempo.............")
            print (".......................................")
            print (".......................................")
            print ("......... No hay prisa.................")
            print (".......................................")
            print (".........¿Ya has terminado?............")

            if(int(input("1.Sí 2.No: "))== 1):
                #Llamamos al método updatePages que nos devolverá False y sacará del bucle, ver método updatePages del fichero Ejercicio2y3.py
                reading = my_lista.updatePages(lectura)#tenemos que parsear el libro de la lista

    elif(operacion == 3):
        print ("¿Estás seguro de que quieres salir?")
        if(int(input("1.Sí 2.No: "))== 1):
            print('Perfecto, nos vemos... "Hack the Planet" ...' )
            bucle = False
        elif(int(input("1.Sí 2.No: "))== 2):
            print("Quedate todo el tiempo que quieras, pero no te acuestes muy tarde...")
        else:
            print("Por favor introduce una opción correcta")
    else:
        print ("Por favor introduce una opción correcta")
