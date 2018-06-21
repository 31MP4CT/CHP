#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                        TRABAJANDO CON SHODAN

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""
        BUSCANDO UN HOST EN CONCRETO
"""""""""""""""""""""""""""""""""""""""""""""""""""

import shodan

# Clave de la API
with open('/root/CHP/SHODAN_KEY', 'r') as key:
    API_KEY = key.readline().rstrip()
    
#Hacemos la conexion con la base de datos de Shodan
ShodanApi = shodan.Shodan(ShodanKeyString)

# Lookup the host
host = ShodanApi.host(str(raw_input('Escribe una dirección IP :')))

# Print general info

print ('IP: %s ' % host['ip_str'])
print ('Organizacion: %s ' % host.get('org', 'n/a'))
print ('Sistema operativo: %s ' % host.get('os', 'n/a'))
for item in host['data']:
    print ('Puerto: %s ' % item['port'])
    print ('Banner: %s ' % item['data'])
