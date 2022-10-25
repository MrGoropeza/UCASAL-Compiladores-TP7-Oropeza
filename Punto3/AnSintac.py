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

from AnLexico import *
import AnLexico

from ply import yacc

def p_S(p):
  '''S : inicioHTML html finHTML'''
  pass
  
def p_html(p):
  '''html : inicioHEAD head finHEAD inicioBODY body finBODY'''
  pass

def p_head(p):
  '''head : inicioTITLE textoPagina finTITLE'''
  pass

def p_body(p):
  '''body : parrafo
          | '''
  pass

def p_parrafo(p):
  '''parrafo : inicioP content finP body'''
  pass

def p_content(p):
  '''content : textoPagina content
             | HR content
             | inicioB content finB content
             | '''
  pass

def p_textoPagina(p):
  '''textoPagina : texto textoPagina
                 | '''
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
