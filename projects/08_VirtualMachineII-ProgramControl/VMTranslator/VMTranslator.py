import os
import sys

import vm_parser
import code_writer
from const import *


def parse_vmfile(vmfile_path, code_writer):
    parser = vm_parser.Parser(vmfile_path)
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
        elif command_type == C_LABEL:
            label = parser.arg1()
            code_writer.write_label(label)
        elif command_type == C_IF:
            label = parser.arg1()
            code_writer.write_if(label)
        elif command_type == C_GOTO:
            label = parser.arg1()
            code_writer.write_goto(label)
        elif command_type == C_FUNCTION:
            function_name = parser.arg1()
            n_vars = parser.arg2()
            code_writer.write_function(function_name, n_vars)
        elif command_type == C_RETURN:
            code_writer.write_return()
        elif command_type == C_CALL:
            function_name = parser.arg1()
            n_args = parser.arg2()
            code_writer.write_call(function_name, n_args)


if __name__ == '__main__':
    input_path = sys.argv[1]

    if os.path.isfile(input_path):    # translate a vm file
        output_file_path = input_path.replace('.vm', '.asm')
        code_writer = code_writer.CodeWriter(output_file_path, need_bootstrap=False)

        current_file_name = os.path.basename(input_path)
        code_writer.set_file_name(current_file_name)

        parse_vmfile(input_path, code_writer)
        code_writer.close()

    elif os.path.isdir(input_path):    # translate vm files in a directory
        output_file_name = os.path.basename(input_path) + '.asm'
        output_file_path = os.path.join(input_path, output_file_name)
        code_writer = code_writer.CodeWriter(output_file_path, need_bootstrap=True)

        for file in os.listdir(input_path):    # tranlate all vm files
            if len(file) > 3 and file[-3:]=='.vm':
                vmfile_path = os.path.join(input_path, file)
                code_writer.set_file_name(file)
                parse_vmfile(vmfile_path, code_writer)
        code_writer.close()
