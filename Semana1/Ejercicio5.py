#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################
#    FUNCIONES
###############################
#Usamos recursividad para obtener el factorial
def factorial(x):
    if(x==0):
        return 1
    else:
        return x * factorial(x-1)

#Función suma
def sum(a,b):
    return a+b
#Funcion resta
def res(a,b):
    return a-b
####################################

print ("Bienvenido a la Calculadora de Python")
print ("Por favor, escoja una operación")
operacion = int(input("1.Suma, 2.Resta, 3.Multiplicación, 4.División, 5.Factorial\n"))
#Opción Suma
if (operacion == 1):
    a = int(input ("Elija el primer sumando: "))
    b = int(input ("Elija el segundo sumando: "))
    print ('%s + %s = %s'  %(a,b,sum(a,b)))
#opción resta
elif (operacion == 2):
    a = int(input ("Elija el minuendo: "))
    b = int(input ("Elija el sustraendo: "))
    print  (str(a) + " - " + str(b) +" = " + '%s' %res(a,b))
#opción multiplicación
elif (operacion == 3):
    a = int(input ("Elija el multiplicando: "))
    b = int(input ("Elija el multiplicador: "))
    print  (str(a) + " * " + str(b) +" = " + '%s' %(a*b))
#opción división
elif (operacion == 4):
    a = int(input ("Elija el dividendo: "))
    b = int(input ("Elija el divisor: "))
    print  (str(a) + " / " + str(b) +" = " + '%s' %(a/b))
#opción factorial
elif (operacion == 5):
    a = int(input ("Elija el número: "))
    print  ( '%s! = %s' %(a,factorial(a)))
#en caso de no ser ninguna de las anteriores
else:
    print ("Por favor escoge alguna de las operaciones anteriores")
