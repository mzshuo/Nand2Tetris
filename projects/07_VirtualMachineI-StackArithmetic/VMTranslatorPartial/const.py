'''
Define some const value of command type.
'''

C_ARITHMETIC = 0
C_PUSH = 1
C_POP = 2
C_LABEL = 3
C_GOTO = 4
C_IF = 5
C_RETURN = 6
C_FUNCTION = 7
C_RETURN = 8
C_CALL = 9

arithmetic_commands = ('add', 'sub', 'neg', 'eq', 'gt', 'lt', 'not', 'and', 'or')

seg_hash = {'local':'LCL', 'argument':'ARG', 'this':'THIS', 'that':'THAT'}
ptr_hash = {'0': 'THIS', '1': 'THAT'}