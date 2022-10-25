# -*- coding: utf-8 -*-
'''
proc id (lista parametros)

Gramática:
  S -> proc id ( L )
  L -> V | C | V, L | C, L
  V -> var id
  C -> const id 
'''
from ply import lex

# Definición de tokens del lenguaje

reserved = {
    'proc' : 'PROC',
    'var' : 'VAR',
    'const' : 'CONST',
}

# 2) Declaración de tokens
tokens = ["id", "coma", "InP", "FinP"] + list(reserved.values())

# 3) Definición de Tokens (ER)
def t_id(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  t.type = reserved.get(t.value,'id')    # Check for reserved words
  return t

t_coma = r","
t_InP=r"\("
t_FinP=r"\)"
t_ignore = r' '



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
