'''
This module is to help resolve symbols in the assembly codes into actual addresses
'''


class SymbolTable:
    '''
    This class is designed to create and maintain the correspondence between symbols and their meaning
    '''

    def __init__(self):
        '''
        Initialize an empty symbol table.
        Add pre-defined symbols into the table.
        '''
        self.empty_addr = 16
        self.symbol_table = {
            'SP': 0,
            'LCL': 1,
            'ARG': 2,
            'THIS': 3,
            'THAT': 4,
            'SCREEN': 16384,
            'KBD': 24576,
        }
        # R0-R15
        for i in range(16):
            self.symbol_table['R'+str(i)] = i

    def addEntry(self, symbol, address=-1):
        '''
        Add the pair (symbol, address) to the table.
        :param symbol: the symbol character (string) to be stored
        :param address: the address character (int) to be binded with the symbol; if address == -1, allocate an empty address automatically.
        '''
        if address == -1:
            address = self.empty_addr
            self.empty_addr += 1
        self.symbol_table[symbol] = address

    def contains(self, symbol):
        '''
        Judge if the symbol table contain the given symbol
        :param symbol: the symbol string to be queried
        :return: True if the symbol has been contained in the table
        '''
        return symbol in self.symbol_table

    def getAddress(self, symbol):
        '''
        Return the address associated with the symbol.
        :param symbol: the symbol string to be queried
        :return: the address (int) associated with the given symbol
        '''
        return self.symbol_table[symbol]
