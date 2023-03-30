import ply.lex as lex
import re
import codecs
import os
import sys

tokens = ['Y','CLASE','ADEMAS','FALSO','PARA','FUN','SI','NULO','O','IMPRIMIR','RETORNAR',
          'SUPER','ESTE','VERDADERO','VAR','MIENTRAS','IDENTIFICADOR','CADENA','NUMERO',
          'REAL','ENTERO','PARENTESIS_IZQUIERDO','PARENTESIS_DERECHO','LLAVE_IZQUIERDA',
          'LLAVE_DERECHA','COMA','PUNTO','PUNTO_Y_COMA','SUMA','RESTA','MULTIPLICACION',
          'DIVISION','NEGACION','DISTINTO','ASIGNACION','IGUALDAD','MENOR_QUE','MENOR_O_IGUAL_QUE',
          'MAYOR_QUE','MAYOR_O_IGUAL_QUE','COMENTARIO','EOF']

reservadas = {
    'y' : 'Y',
    'clase' : 'CLASE',
    'ademas' : 'ADEMAS',
    'falso' : 'FALSO',
    'para' : 'PARA',
    'fun' : 'FUN',
    'si' : 'SI',
    'nulo' : 'NULO',
    'o' : 'O',
    'imprimir' : 'IMPRIMIR',
    'retornar' : 'RETORNAR',
    'super' : 'SUPER',
    'este' : 'ESTE',
    'verdadero' : 'VERDADERO',
    'var' : 'VAR',
    'mientras' : 'MIENTRAS'
}

tokens = tokens + list(reservadas.values())

ignorar_caract = '\t'
token_SUMA = r'\+'
token_RESTA = r'\-'
token_MULTIPLICACION = r'\*'
token_DIVISION = r'/'
token_ASIGNACION = r'='

