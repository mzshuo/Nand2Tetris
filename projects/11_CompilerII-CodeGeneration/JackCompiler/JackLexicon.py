from enum import Enum


class TokenType(Enum):
    '''
    Constant values of token types.
    '''
    KEYWORD = 0
    SYMBOL = 1
    IDENTIFIER = 2
    INT_CONST = 3
    STRING_CONST = 4


class VarType(Enum):
    '''
    Constant values of variable types.
    '''
    STATIC = "STATIC"
    FIELD = "FIELD"
    ARG = "ARG"
    LCL = "LCL"


class SegmentType(Enum):
    '''
    Constant values of segment types.
    '''
    CONSTANT = "constant"
    ARGUMENT = "argument"
    LOCAL = "local"
    STATIC = "static"
    THIS = "this"
    THAT = "that"
    POINTER = "pointer"
    TEMP = "temp"


class CommandType(Enum):
    '''
    Constant values of command types.
    '''
    ADD = 'add'
    SUB = 'sub'
    NEG = 'neg'
    EQ = 'eq'
    GT = 'gt'
    LT = 'lt'
    AND = 'and'
    OR = 'or'
    NOT = 'not'


# Token catogery
keyword = ('class', 'constructor', 'function', 'method', 'field', 'static', 
           'var', 'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this', 
           'let', 'do', 'if', 'else', 'while', 'return')
symbol = ('{', '}', '[', ']', '(', ')', '.', ',', ';', 
          '+', '-', '*', '/', '&', '|', '~', '>', '<', '=')
op = ('+', '-', '*', '/', '&', '|', '>', '<', '=')
unaryOp = ('-', '~')



