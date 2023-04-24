# To run this assembler, type 'python assembler.py file_path' in the command line.

import Parser
import Code
import SymbolTable

import sys
import os

if __name__ == '__main__':
    file_path = sys.argv[1]
    parser = Parser.Parser(file_path)
    symbol_table = SymbolTable.SymbolTable()
    output = []

    # first pass: store all label symbols and addresses within assembly codes into the symbol table
    line_number = -1
    while(parser.hasMoreCommands()):
        parser.advance()
        cmd_type = parser.commandType()

        if cmd_type != 'L_COMMAND':
            line_number += 1

        if cmd_type == 'L_COMMAND':
            symbol = parser.symbol()
            symbol_table.addEntry(symbol, line_number + 1)

    # second pass: translate assembly codes into binary machine codes including symbols
    parser.restart()
    while (parser.hasMoreCommands()):
        parser.advance()
        cmd_type = parser.commandType()
        bits = ''

        if cmd_type == 'L_COMMAND':
            continue
        elif cmd_type == 'A_COMMAND':
            symbol = parser.symbol()
            if not symbol.isdigit():
                if not symbol_table.contains(symbol):
                    symbol_table.addEntry(symbol)
                symbol = symbol_table.getAddress(symbol)
            addr = bin(int(symbol)).replace('0b', '')
            bits = '0' + addr.rjust(15, '0')
        elif cmd_type == 'C_COMMAND':
            c = parser.comp()
            d = parser.dest()
            j = parser.jump()
            cc = Code.comp(c)
            dd = Code.dest(d)
            jj = Code.jump(j)
            bits = '111' + cc + dd + jj

        output.append(bits)

    # ouuput hack code into the same place as the asm code
    output = '\n'.join(output)
    dir_path = os.path.dirname(file_path)
    output_file_name = os.path.basename(file_path).replace('.asm', '.hack')
    output_file_path = os.path.join(dir_path, output_file_name)
    with open(output_file_path, 'w') as file:
        file.write(output)
