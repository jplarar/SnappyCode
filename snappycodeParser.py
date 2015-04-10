# snappycodeParser.py

from ply.lex import TOKEN
import sys
import snappycodeLex
import fileinput
from cuadruplo import *
from procVarTables import *
from memoria import *
from cubosemantico import *


tokens = snappycodeLex.tokens
actualProc = "global"
memoria = 0
pilaOperadores = []
pilaOperandos = []
tempCont = 0
cuadruplos = []
cuadCont = 0 

precedence = (
    ('nonassoc', 'MAYORQUE', 'MENORQUE', 'DIFERENTEQUE', 'IGUALQUE', 'MAYORIGUAL', 'MENORIGUAL'),
    ('left','MAS','MENOS'),
    ('left','MULT','DIV'),
    ('right','UMINUS'),
    )



def p_program(t): 
    'program : INICIOPROGRAMA vars cuerpo FINPROGRAMA'
    pass


def p_vars(t): 
    'vars : vars CREAR tipo ID PUNTOCOMA '
    global memoria
    if actualProc == 'global':
      asigna_memoria_global(t[3])
      varGlbInsert(t[4], None, t[3], memoria)
    else:
      asigna_memoria_local(t[3])
      varLocInsert(t[4], None, t[3], memoria, actualProc)
    pass

def p_tipo(t):
    '''tipo   : ENTERO
              | FLOTANTE
              | TEXTO
              | BOOLEANO
              | LISTA '''
    t[0] = t[1]
    pass

def p_vars_empty(t): 
    'vars : empty'

def p_empty(t):
    'empty : '
    pass

 
def p_cuerpo(t): 
    'cuerpo : cuerpo_func principal'
    global procTable
    procPrint(procTable)
    global cuadruplos
    for cuad in cuadruplos:
        print ("Cuadruplos")
        print(cuad.num, '-', cuad.opt, '-', cuad.opd1, '-', cuad.opd2, '-', cuad.res , '\n')
    pass
 
def p_cuerpo_func(t): 
    '''cuerpo_func : cuerpo_func funcion 
         | empty'''
    pass
 
def p_funcion(t):
    'funcion : iniciofunc param vars finfunc'
    pass

def p_iniciofunc(t): 
    'iniciofunc : INICIOFUNCION tipo ID'
    t[0]= t[3]
    global scope
    scope = 'parametro'
    global actualProc
    actualProc = t[3]
    pDir = 0
    procInsert(actualProc, t[2], pDir)
    pass

def p_param(t): 
    'param : PARAMETROS tipo ID param_mult'
    global scope
    scope = 'local'
    global memoria
      #params[t[3]] = {'type' : t[2]}
    asigna_memoria_local(t[2])
    paramInsert(t[3], t[2], memoria, actualProc)
    pass
     
 
def p_param_mult(t): 
    'param_mult : COMA tipo ID param_mult'
    global memoria
    asigna_memoria_local(t[2])
    paramInsert(t[3], t[2], memoria, actualProc)
    pass

def p_param_mult_empty(t): 
    'param_mult : empty'
    pass

def p_param_empty(t): 
    'param : empty'
    pass 


def p_finfunc(t): 
    'finfunc : C REGRESA expresion FINFUNCION'
    pass

 
def p_C(t): 
    '''C : C estatuto 
           | empty'''
    pass
 
 
def p_estatuto(t): 
    '''estatuto : asignacion
           | condicion
           | ciclo
           | io
           | accion'''
    pass
 
def p_asignacion(t): 
    'asignacion : ID IGUAL expresion PUNTOCOMA'
    pass
 

def p_expresion_eval(t): 
    '''expresion : exp MAYORQUE exp
           | exp MENORQUE exp
           | exp DIFERENTEQUE exp
           | exp IGUALQUE exp
           | exp MAYORIGUAL exp
           | exp MENORIGUAL exp'''
    if t[2] == '>'  : t[0] = t[1] > t[3]
    elif t[2] == '<': t[0] = t[1] < t[3]
    elif t[2] == '!=': t[0] = t[1] != t[3]
    elif t[2] == '==': t[0] = t[1] == t[3]
    elif t[2] == '>=': t[0] = t[1] >= t[3]
    elif t[2] == '<=': t[0] = t[1] <= t[3]
    pass

def p_exp_agrupacion(t): 
    'exp : PARENTIZQ expresion PARENTDER'
    t[0] = t[2]
    pass

def p_exp_binop(t):
    '''exp : exp MAS push_opt exp
           | exp MENOS push_opt exp
           | exp MULT push_opt exp
           | exp DIV push_opt exp'''
    global cuadruplos
    global pilaOperandos
    global pilaOperadores
    global memoria
    global tempCont
    global cuadCont
    
    if pilaOperadores:
      operador = pilaOperadores.pop()
      operando2 = pilaOperandos.pop()
      operando1 = pilaOperandos.pop()

      op1Name = ''
      op2Name = ''

      if isinstance(operando1,varTableNode):
        op1Name = operando1.varName
        operando1 = operando1.varVal
      if isinstance(operando2,varTableNode):
        op2Name = operando2.varName
        operando2 = operando2.varVal

      type2 = getType(operando2)
      type1 = getType(operando1)

      resType = cubo_semantico[type1][type2][operador]

      if resType != "error":
        if operador == '+':
          resultado = operando1 + operando2
        elif operador == '-':
          resultado = operando1 - operando2
        elif operador == '*':
          resultado = operando1 * operando2
        elif operador == '/':
          resultado = operando1 / operando2

        asigna_memoria_constante(resType)
        consInsert(resultado, resType, memoria)
        asigna_memoria_temporal(resType)

        operandoTemp = varTableNode('t'+str(tempCont), resultado, resType, memoria)

        op1Dir = consGetDir(operando1)
        op2Dir = consGetDir(operando2)
        resDir = consGetDir(resultado)
        cuadruplo = Cuadruplo(cuadCont, operador, op1Dir, op2Dir, resDir)
        cuadruplos.append(cuadruplo)

        pilaOperandos.append(operandoTemp)
        tempCont += 1
        cuadCont += 1
        t[0]=t[1]


      else:
        print("Error Semantico: valores incompatibles en suma")    
    pass

def p_push_opt(t):
    'push_opt : '
    global pilaOperadores
    pilaOperadores.append(t[-1])


def p_exp_uminus(t):
    'exp : MENOS exp %prec UMINUS'
    t[0] = -t[2]
 


def p_exp_int(t):
    'exp : CTEENTERO push_opd'
    global memoria
    asigna_memoria_constante('entero')
    consInsert(t[1],'entero',memoria)
    t[0] = t[1]

def p_push_opd(t):
    'push_opd : '
    pilaOperandos.append(t[-1])
    pass

def p_exp_float(t):
    'exp : CTEFLOTANTE push_opd'
    global memoria
    asigna_memoria_constante('flotante')
    consInsert(t[1],'flotante',memoria)

    t[0] = t[1]
    pass

def p_exp_booleano(t):
    '''exp : TRUE push_opd
          | FALSE push_opd '''
    t[0]=t[1]
    global memoria
    asigna_memoria_constante('booleano')
    consInsert(t[1],'booleano',memoria)
    pass

def p_exp_var(t):
    'exp : ID'
    try:
        #print (procTable[scope])
        t[0] = 1
    except LookupError:
        print("Undefined name '%s'" % t[1])
        t[0] = 0
 
def p_exp_texto(t):
    '''exp : CTETEXTO push_opd
           | llamada '''
    t[0] = t[1]
    global memoria
    asigna_memoria_constante('texto')
    consInsert(t[1],'texto',memoria)
pass

def p_exp_texto(t):
    'exp :  llamada'
    t[0] = t[1]
pass

def p_llamada(t):
    'llamada : ID llamada_param'
pass

def p_llamada_param(t):
    '''llamada_param : PARAMETROS expresion llamada_param_mult
           | empty  '''
pass
def p_expresion_empty(t): 
    '''expresion : exp '''
    t[0] = t[1]
    pass
 

def p_llamada_param_mult(t):
    '''llamada_param_mult :  llamada_param_mult COMA expresion 
           | empty  '''
pass
 
def p_condicion(t):
    'condicion : SI expresion ENTONCES bloque condicion_else FINSI'
    pass
 
def p_bloque(t):
    'bloque   : INICIOBLOQUE bloque_estatuto_mult FINBLOQUE'
    pass

def p_bloque_estatuto_mult(t):
    '''bloque_estatuto_mult        : bloque_estatuto_mult estatuto 
               | empty '''
    pass

def p_condicion_else(t):
    '''condicion_else : SINO bloque
               | empty '''
    pass
 
def p_ciclo(t):
    'ciclo    : MIENTRAS expresion HACER bloque FINMIENTRAS'
    pass


 
def p_io(t):
    '''io : PEDIRALUSUARIO ID
               | DECIRALUSUARIO expresion '''
    pass
 
def p_accion(t):
    'accion   : tipo_accion O ID PUNTOCOMA'
    pass
 
def p_tipo_accion(t):
    '''tipo_accion : lista
               | objeto '''
    pass

def p_lista(t):
    '''lista    : AGREGAR
               | SACAR
               | VER '''
    pass
 
def p_objeto(t):
    '''objeto   : CREAR
               | DIBUJAR
               | BORRAR
               | GIRAR
               | PINTAR
               | DESPINTAR
               | MOVER '''
    pass
 
def p_O(t):
    '''O        : X expresion
               | Y expresion
               | DERECHA
               | IZQUIERDA
               | ARRIBA
               | ABAJO
               | empty  '''
    pass
 

def p_principal(t): 
    'principal : iniciomain vars C FINPRINCIPAL'

    pass

def p_iniciomain(t): 
    'iniciomain : INICIOPRINCIPAL'
    global actualProc
    actualProc = 'main'
    pDir = 0
    procInsert(actualProc, actualProc, pDir)
    pass


def p_error(p):
    if p:
        print("Error de sintaxis en: '%s'" % p.value + p.type)
    else:
        print("Error de sintaxis")

def asigna_memoria_global(tipo):
    global EnteroGlobal
    global FlotanteGlobal
    global TextoGlobal
    global BooleanGlobal
    global memoria 
    if tipo == 'entero' or tipo == 'ENTERO':
      memoria = EnteroGlobal
      EnteroGlobal += 1
    elif tipo == 'flotante' or tipo == 'FLOTANTE':
      memoria = FlotanteGlobal
      FlotanteGlobal += 1
    elif tipo == 'texto' or tipo == 'TEXTO':
      memoria = TextoGlobal
      TextoGlobal += 1
    elif tipo == 'booleano' or tipo == 'BOOLEANO':
      memoria = BooleanGlobal
      BooleanGlobal += 1

def asigna_memoria_local(tipo):
    global EnteroLocal
    global FlotanteLocal
    global TextoLocal
    global BooleanLocal
    global memoria 
    if tipo == 'entero' or tipo == 'ENTERO':
      memoria = EnteroLocal
      EnteroLocal += 1
    elif tipo == 'flotante' or tipo == 'FLOTANTE':
      memoria = FlotanteLocal
      FlotanteLocal += 1
    elif tipo == 'texto' or tipo == 'TEXTO':
      memoria = TextoLocal
      TextoLocal += 1
    elif tipo == 'booleano' or tipo == 'BOOLEANO':
      memoria = BooleanLocal
      BooleanLocal += 1

def asigna_memoria_constante(tipo):
    global EnteroConstante
    global FlotanteConstante
    global TextoConstante
    global BooleanConstante
    global memoria 
    if tipo == 'entero' or tipo == 'ENTERO':
      memoria = EnteroConstante
      EnteroConstante += 1
    elif tipo == 'flotante' or tipo == 'FLOTANTE':
      memoria = FlotanteConstante
      FlotanteConstante += 1
    elif tipo == 'texto' or tipo == 'TEXTO':
      memoria = TextoConstante
      TextoConstante += 1
    elif tipo == 'booleano' or tipo == 'BOOLEANO':
      memoria = BooleanConstante
      BooleanConstante += 1

def asigna_memoria_temporal(tipo):
    global EnteroTemporal
    global FlotanteTemporal
    global TextoTemporal
    global BooleanTemporal
    global memoria 
    if tipo == 'entero' or tipo == 'ENTERO':
      memoria = EnteroTemporal
      EnteroTemporal += 1
    elif tipo == 'flotante' or tipo == 'FLOTANTE':
      memoria = FlotanteTemporal
      FlotanteTemporal += 1
    elif tipo == 'texto' or tipo == 'TEXTO':
      memoria = TextoTemporal
      TextoTemporal += 1
    elif tipo == 'booleano' or tipo == 'BOOLEANO':
      memoria = BooleanTemporal
      BooleanTemporal += 1

import ply.yacc as yacc
yacc.yacc(method = 'LALR')

program = []
for line in fileinput.input():
	program.append(line)
yacc.parse(' '.join(program))

