# -*- coding: utf-8 -*-

'''
Gramática:
  E → E + T | T
  T → T * F | F
  F → num | ( E )
'''

'''
Gramática Limpia:
  E → T E'
  E' → + T E' | epsilon
  T → F T'
  T' → * F T' | epsilon
  F → num | ( E )
'''
from AnLexico import *
import AnLexico

from ply import yacc

def p_E(p):
  '''E : T Eprima'''
  pass

def p_Eprima(p):
  '''Eprima : sum T Eprima
            | '''
  pass

def p_T(p):
  '''T : F Tprima'''
  pass

def p_Tprima(p):
  '''Tprima : times F Tprima
            | '''
  pass

def p_F(p):
  '''F : num
       | InP E FinP'''
  pass

def p_error(p):
  print("Error sintáctico en la línea: " + str(p.lineno)
         + ". No se esperaba el token: " + str(p.value))    
  raise Exception('syntax', 'error')
   
#Construcción del parser:  

parser = yacc.yacc() 

#Inicializa el contador de líneas
AnLexico.lexer.lineno=0
