#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argsparse
import os

"""
 Esta clase contiene en el main del programa y define los métodos para el parseo
 de argumentos y las funciones que debera llevar a cabo la herramienta.
"""

def parser():
    """
     Define los argumentos con los que el usuario deberá utilizar la herramienta.
    """
    parser = argsparse.ArgumentParser(description='Esta herramienta permite la obtención \
                                      de información tanto de un domino como de un host \
                                      específico. Por defecto las búsquedas se realizarán \
                                      contra Shodan y Whois. Ver comandos para más opciones.')

    parser.add_argument("-ip", "--ip_address", type=str,
                        help="Dirección IP del equipo cuya información quieres obtener.")
    parser.add_argument("-d", "--domain", type=str,
                        help="Nombre del dominio cuya información quieres obtener.")
    parser.add_argument("shodan_query", type=str,
                        help="Búsqueda empleando Shodan")
    parser.add_argument("-g", "--geo", action='store_true',
                        help="Utiliza esta opción para activar la Geolocalización")
    parser.add_argument("-D", "--dns", action='store_true',
                        help="Utiliza esta opción para activar la consulta DNS."
    parser.add_argument("-f", "--facets", action='store_true',
                        help="Utiliza esta opción para devolver los FACETS de Shodan \
                        asociados a esta búsqueda")
    args=parser.parse_args()
    return args

def module_execution(*args):
    """
     Ejecta los scripts asociados (Shodan, Whois, DNS, etc) en función de los \
     argumentos introducidos por el usuario.
    """
    # Filtra las opciones en función del parser y devuelve el nombre del script que deberá ejecutarse
    if args.ip_address:
        function =
        pass
    elif args.domain:
        pass
    elif args.facets:
        pass

   # Filtra las opciones parseadas y devuelve -si fuera necesario- las opciones adicionales del comando.
   
