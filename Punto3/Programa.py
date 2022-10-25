# -*- coding: utf-8 -*-

'''
Gramática:
  S -> InHtml html FinHtml
  html -> InHead head FinHead InBody body FinBody
  head -> InTitle texto FinTitle
  body -> epsilon | parrafo
  parrafo -> InP content FinP body
  content -> texto content | InHR content | InB content FinB content | epsilon
  texto -> [a-zA-Z0-9] texto
'''

import os, sys

from AnSintac import parser

filename = os.path.join(sys.path[0], "ej.txt")     #cambiar este nombre para probar otros ejemplos

try:
    f = open(filename)    
    data = f.read()
    f.close()
    print('Contenido del archivo:\n',data,'\n')  #visualizar las instrucciones contenidas en el archivo
except IndexError:
    print('Error en archivo:\n')
    data = ''

#analisis sintactico
try:
        resultado = parser.parse(data)
        print('¡Analisis sintactico correcto!')     
except:
        print('Analisis sintactico incorrecto')

