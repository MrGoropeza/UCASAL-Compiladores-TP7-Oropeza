# -*- coding: utf-8 -*-
from ply import lex

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

# Definición de tokens del lenguaje

tokens = [
    "texto", 
    "inicioHTML", "finHTML",
    "inicioHEAD", "finHEAD",
    "inicioTITLE", "finTITLE",
    "inicioBODY", "finBODY",
    "inicioP", "finP",
    "inicioB", "finB",
    "HR"
]

t_texto = r"[a-zA-Z0-9][a-zA-Z0-9]+"

t_inicioHTML = r"(<HTML>)"
t_finHTML = r"(</HTML>)"

t_inicioHEAD = r"(<HEAD>)"
t_finHEAD = r"(</HEAD>)"

t_inicioTITLE = r"(<TITLE>)"
t_finTITLE = r"(</TITLE>)"

t_inicioBODY = r"(<BODY>)"
t_finBODY = r"(</BODY>)"

t_inicioP = r"(<P>)"
t_finP = r"(</P>)"

t_inicioB = r"(<B>)"
t_finB = r"(</B>)"

t_HR = r"(<HR>)"

t_ignore = r'[ ]+'



# 4) Definir la función t_error para el tratamiento de errores.
def t_error(t):
    print("__________________")
    print("Error: %s en linea %s" % (repr(t.value[0]), lexer.lineno))
    t.lexer.skip(1)

# 5) Definir la función t_newline para el contador de linea   
def t_newline(t):
  r'\n'
  t.lexer.lineno+=1


# 6) Construcción del analizador léxico
lexer = lex.lex()
