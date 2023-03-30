import ply.lex as lex
import re
import codecs
import os
import sys

#CREACION DE LISTA PARA PALABRAS RESERVADAS
reservadas = [
	'Y',
    'CLASE',
    'ADEMAS',
    'FALSO',
    'PARA',
    'FUN',
    'SI',
    'NULO',
    'O',
    'IMPRIMIR',
    'RETORNAR',
    'SUPER',
    'ESTE',
    'VERDADERO',
    'VAR',
    'MIENTRAS'
]

#CREACION DE LISTA PARA TOKENS 
tokens = reservadas+['IDENTIFICADOR','CADENA','NUMERO',
          'REAL','ENTERO','PARENTESIS_IZQUIERDO','PARENTESIS_DERECHO','LLAVE_IZQUIERDA',
          'LLAVE_DERECHA','COMA','PUNTO','PUNTO_Y_COMA','SUMA','RESTA','MULTIPLICACION',
          'DIVISION','NEGACION','DISTINTO','ASIGNACION','IGUALDAD','MENOR_QUE','MENOR_O_IGUAL_QUE',
          'MAYOR_QUE','MAYOR_O_IGUAL_QUE','COMENTARIO','EOF']

#EXPRESIONES REGULARES PARA ASIGNAR LOS CARACTERES A LOS TOKENS
ignorarcaract = '\t '
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_ASIGNACION = r'='
t_MENOR_QUE = r'<'
t_MENOR_O_IGUAL_QUE = r'<='
t_MAYOR_QUE = r'>'
t_MAYOR_O_IGUAL_QUE = r'>='
t_PARENTESIS_IZQUIERDO = r'\('
t_PARENTESIS_DERECHO = r'\)'
t_COMA = r','
t_PUNTO_Y_COMA = r';'
t_PUNTO= r'\.'
t_NEGACION = r'!'
t_DISTINTO = r'!='
t_IGUALDAD = r'=='
t_LLAVE_IZQUIERDA = r'{'
t_LLAVE_DERECHA = r'}'

#FUNCIONES PARA IDENTIFICAR IDENTIFICADORES, NUMEROS, COMENTARIOS, ESPACIOS EN BLANCO, SALTOS DE LINEA Y ERRORES
def t_IDENTIFICADOR(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if t.value.upper() in reservadas:
		t.value = t.value.upper()
		#reservadas.get(t.value,'ID')
		t.type = t.value

	return t

def t_NUEVALINEA(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_ESPACIOENBLANCO(t):
 r'\s+'
 pass

#dsfjksdlgjklsdgjsdgslxcvjlk-,.
def t_COMENTARIO(t):
	r'\//.*'
	pass

def t_COMENTARIOMULTLINEA(t):
	r'(\/\*(\s*|.*?)*\*\/)|(\/\/.*)'
	pass


def t_NUMERO(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_error(t):
	print("caracter ilegal '%s'" % t.value[0])
	t.lexer.skip(1)
