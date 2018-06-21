#!/usr/bin/env python
# -*- coding: utf-8 -*-


import shodan
import sys

# Clave de la API
with open('/root/CHP/SHODAN_KEY', 'r') as key:
    API_KEY = key.readline().rstrip()

# Definimos los facets que podemos utilizar para filtrar las busquedas
# Por defecto los facets nos muestran solo el top 5 de cada categoría.
# Esto lo podemos modificar tal que así ('country',3), para añadir más
# o menos busquedas.
FACETS = [
    'org',
    'domain',
    'port',
    'asn',
    'country',
]

# La explicación de cada uno de los facets.
# Modificar en caso de cambiar el número de busquedas.
FACET_TITLES = {
    'org': 'Top 5 Organizations',
    'domain': 'Top 5 Domains',
    'port': 'Top 5 Ports',
    'asn': 'Top 5 Autonomous Systems',
    'country': 'Top 5 Countries',
}

# Comprobamos que el argumento introducido por consola es correcto
if len(sys.argv) == 1:
    print 'Usage: %s <search query>' % sys.argv[0]
    sys.exit(1)

try:
    # Realizamos la conexion con la base de datos de Shodan
    api = shodan.Shodan(API_KEY)

    # Generamos una búsqueda con el argumento introducido por consola
    query = ' '.join(sys.argv[1:])

    # Usamos el método count(), que sin ser de pago es más rápido que search()
    # y nos permite usar los facets.
    result = api.count(query, facets=FACETS)

    # Mostramos un pequeño resumen del proceso (Input/Output)
    print 'Shodan Summary Information'
    print 'Query: %s' % query
    print 'Total Results: %s\n' % result['total']

    # Mostramos el resultado de los FACETS
    for facet in result['facets']:
        print FACET_TITLES[facet]

        for term in result['facets'][facet]:
            print '%s: %s' % (term['value'], term['count'])

        # Una linea vacía para la comodidad en la lectura.
        print ''

except Exception, e:
    print 'Error: %s' % e
    sys.exit(1)
