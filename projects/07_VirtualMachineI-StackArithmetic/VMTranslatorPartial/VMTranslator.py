import os
import sys

import vm_parser
import code_writer
from const import *


if __name__ == '__main__':
    input_path = sys.argv[1]
    parser = vm_parser.Parser(input_path)

    output_file_path = input_path.replace('.vm', '.asm')
    code_writer = code_writer.CodeWriter(output_file_path)

    while(parser.has_more_lines()):
        parser.advance()
        command_type = parser.command_type()
        if command_type == C_ARITHMETIC:
            command = parser.arg1()
            code_writer.write_arithmetic(command)
        elif command_type == C_PUSH or command_type == C_POP:
            segment = parser.arg1()
            index = parser.arg2()
            code_writer.write_push_pop(command_type, segment, index)

    code_writer.close()