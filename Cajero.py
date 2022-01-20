# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

leersaldo = open('saldo.txt', 'r')
saldo= int ((leersaldo.read()))
leersaldo.close()


preguntaInicial = int (input ("Que desea hacer: 1 Depositar 2 Retirar "))


if preguntaInicial==1:
    deposito = int (input ("Cuanto desea depositar? "))
    saldo = saldo + deposito
    grabarsaldo = open('saldo.txt', 'w')
    grabarsaldo.write(str(saldo))
    grabarsaldo.close()
if preguntaInicial==2:
    retiro = int (input ("Cuanto desea retirar? "))
    if saldo<retiro:
        print ("Saldo insuficiente")
    else:
        saldo = saldo - retiro
        grabarsaldo = open('saldo.txt', 'w')
        grabarsaldo.write(str(saldo))
        grabarsaldo.close()

        
