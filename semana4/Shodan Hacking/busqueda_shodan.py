#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                        TRABAJANDO CON SHODAN

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""
                BUSCANDO CON SHODAN
"""""""""""""""""""""""""""""""""""""""""""""""""""

import shodan

# Clave de desarrollador de la API de shodan
# Clave de la API
with open('/root/CHP/SHODAN_KEY', 'r') as key:
    API_KEY = key.readline().rstrip()

#Realizamos la conexion con la base de datos de Shodan
ShodanApi = shodan.Shodan(ShodanKeyString)

# Ponemos el código entre un try/catch para manejar las excepciones
try:
    # Buscamos en Shodan con el método WebAPI.search()
    busqueda = str(raw_input("Introduce la cadena a buscar en shodan: "))
    resultados = ShodanApi.search(busqueda)

    # Mostramos el resultado
    print ('Cantidad de resultados encontrados: %s' % resultados['total'])
    for i in resultados['matches']:
        print ('IP: %s' % i['ip_str'])
        print ('Data: %s' % i['data'])
        print ('Hostnames: %s' % i['hostnames'])
        print ('Puerto: %s' % i['port'])
        print ('')

except shodan.APIError as e:
    print ('Ups! Ha ocurrido un error: %s' % e)
