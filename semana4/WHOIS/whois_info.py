#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                        TRABAJANDO CON PYTHONWHOIS

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import pythonwhois
from termcolor import colored       #Libreria para colores

#Utilizamos la API de pythonwhois para extraer información desde cualquier script en Python
"""Pedimos al usuario el nombre de un dominio"""
dominio = str(raw_input('Escribe el nombre de un domino(e.g: google.com): ' ))

"""Recuperamos el servidor raiz para un dominio determinado"""
pythonwhois.net.get_root_server(dominio)

"""Obtenemos un diccionario con toda la información sobre el dominio"""
whois = pythonwhois.get_whois(dominio)

"""Obtenemos la información del dominio de manera 'cruda'"""
whois_raw = pythonwhois.net.get_whois_raw(dominio)

print (colored("\nValores de keys para el servidor: ",'red',attrs=['bold', 'blink']))
print (whois.keys())

print (colored("\nValores de la búsqueda para el servidor: ",'red',attrs=['bold', 'blink']))
print (whois.values())

print (colored("\nValores de la búsqueda para el servidor crudo: ",'red',attrs=['bold', 'blink']))
print(whois_raw)
