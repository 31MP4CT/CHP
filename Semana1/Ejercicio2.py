#!/usr/bin/env python
# -*- coding: utf-8 -*-
cadena_opciones = ['Capitalize', 'Isalnum', 'Isalpha', 'Isupper', 'Lower', 'Rstrip']
cadena_lista = ['hola python ', 'HOLA PYTHON ', 'H074PY7H0N', '  hoLA  pYtHon   ']

print (cadena_lista)
print (cadena_opciones)
for i in range(len(cadena_lista)):

#Imprime la cadena de texto con el primer caracter mayúscula y el resto minúscula
    print(cadena_lista[i].capitalize()),
#Devuelve true si la cadena es alfa-númerica
    print (cadena_lista[i].isalnum()),
#Devuelve true si la cadena es alfabética
    print(cadena_lista[i].isalpha()),
#Devuelve true si la cadena es todo mayúscula
    print(cadena_lista[i].isupper()),
#Imprime la cadena todo en minúsculas
    print(cadena_lista[i].lower()),
#Devuelve la cadena sin espacios al final
    print(cadena_lista[i].rstrip())