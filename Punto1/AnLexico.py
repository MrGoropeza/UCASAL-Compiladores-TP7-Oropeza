# -*- coding: utf-8 -*-
'''
Gramática:
  E → E + T | T
  T → T * F | F
  F → num | ( E )
'''
from ply import lex

# Definición de tokens del lenguaje

# 2) Declaración de tokens
tokens = ["sum", "times", "num", "InP", "FinP"]

# 3) Definición de Tokens (ER)
t_sum = r"\+"
t_times = r"\*"
t_num = r"[0-9]+"
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
