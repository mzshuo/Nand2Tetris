from JackLexicon import VarType


class SymbolTable:
    '''
    Created for a class or a subroutine to preserve symbols and their type, kind, and index.
    Class-level symbol table: preserves field and static variables;
    Subroutine-level symbol table: preserves argument and local variables.
    '''

    def __init__(self):
        '''
        Creates a new symbol table.
        '''
        self.table = {}
        self.cnter = {VarType.STATIC: 0,
                      VarType.FIELD: 0,
                      VarType.ARG: 0,
                      VarType.LCL: 0}    # only two of these four should be used

    def reset(self):
        '''
        Empties the symbol table, and resets the four indexes to 0.
        Should be called when starting to compile a subroutine declaration.
        '''
        self.table.clear()
        for key in self.cnter.keys():
            self.cnter[key] = 0

    def define(self, name, type, kind):
        '''
        Defines (adds to the table) a new variable with given name, type and kind.
        Assigns to it the index value of that kind, and adds 1 to the index.
        '''

        self.table[name] = {'type': type, 'kind': kind, 'index': self.cnter[kind]}
        self.cnter[kind] += 1

    def var_count(self, kind):
        '''
        Returns the number of variables of the given kind already defined in the table.
        '''
        return self.cnter[kind]

    def kind_of(self, name):
        '''
        Returns the kind of the named identifier.
        If the identifier is not found, returns NONE.
        '''
        return self.table[name]['kind']

    def type_of(self, name):
        '''
        Returns the type of the named variable.
        '''
        return self.table[name]['type']

    def index_of(self, name):
        '''
        Returns the index of the named variable.
        '''
        return self.table[name]['index']

    def find(self, name):
        '''
        Returns if name is in the symbol table.
        '''
        return name in self.table.keys()