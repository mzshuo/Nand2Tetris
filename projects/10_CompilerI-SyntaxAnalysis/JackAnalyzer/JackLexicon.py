# Constant value of token type
KEYWORD = 0
SYMBOL = 1
IDENTIFIER = 2
INT_CONST = 3
STRING_CONST = 4


# Token catogery
keyword = ('class', 'constructor', 'function', 'method', 'field', 'static', 
           'var', 'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this', 
           'let', 'do', 'if', 'else', 'while', 'return')
symbol = ('{', '}', '[', ']', '(', ')', '.', ',', ';', 
          '+', '-', '*', '/', '&', '|', '~', '>', '<', '=')
op = ('+', '-', '*', '/', '&', '|', '>', '<', '=')
unaryOp = ('-', '~')


