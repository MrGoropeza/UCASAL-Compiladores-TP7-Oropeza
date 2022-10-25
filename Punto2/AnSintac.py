# -*- coding: utf-8 -*-

'''
proc id (lista parametros)

Gramática:
  S -> proc id ( L )
  L -> V | C | V, L | C, L
  V -> var id
  C -> const id 
'''

from AnLexico import *
import AnLexico

from ply import yacc

def p_S(p):
  '''S : PROC id InP L FinP'''
  pass
  
def p_L(p):
  '''L : V
       | C
       | V coma L
       | C coma L'''
  pass

def p_V(p):
  '''V : VAR id'''
  pass

def p_C(p):
  '''C : CONST id'''
  pass

def p_error(p):
  if(p == None): print("Se esperaban más tokens")
  print("Error sintáctico en la línea: " + str(p.lineno)
         + ". No se esperaba el token: " + str(p.value))    
  raise Exception('syntax', 'error')
   
#Construcción del parser:  

parser = yacc.yacc() 

#Inicializa el contador de líneas
AnLexico.lexer.lineno=0
