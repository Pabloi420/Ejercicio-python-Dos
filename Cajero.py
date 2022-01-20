# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

leersaldo = open('saldo.txt', 'r')
saldo= int ((leersaldo.read()))
leersaldo.close()
leerclave=open('clave.txt', 'r')
clave=leerclave.read()
leerclave.close()

preguntaInicial = int (input ("Que desea hacer: 1 Depositar 2 Retirar 3 Modificar clave "))


if preguntaInicial==1:
    deposito = int (input ("Cuanto desea depositar? "))
    saldo = saldo + deposito
    grabarsaldo = open('saldo.txt', 'w')
    grabarsaldo.write(str(saldo))
    grabarsaldo.close()
    print ("Su saldo ahora es de", saldo)
if preguntaInicial==2:
    retiro = int (input ("Cuanto desea retirar? "))
    if saldo<retiro:
        print ("Saldo insuficiente")
    else:
        saldo = saldo - retiro
        grabarsaldo = open('saldo.txt', 'w')
        grabarsaldo.write(str(saldo))
        grabarsaldo.close()
if preguntaInicial==3:
    corroborar = input ("Ingrese su actual clave: ")
    if corroborar==clave:
        nuevaClave=input ("Ingrese nueva clave: ")
        corroborarnuevaclave=input ("Ingrese nuevamente ")
        if nuevaClave==corroborarnuevaclave:
            clave=nuevaClave
            grabarclave = open('clave.txt', 'w')
            grabarclave.write(str(clave))
            grabarclave.close()
            print ("Ingreso correctamente nueva clave ")
        else:
            print ("No ingreso correctamente nueva clave")
    
        
