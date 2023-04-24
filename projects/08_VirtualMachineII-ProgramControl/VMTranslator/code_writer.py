from const import *
import os


class CodeWriter:
    '''
    Write the assembly code that implements the parsed command.
    '''

    def __init__(self, output_file_path, need_bootstrap=True):
        '''
        Open an output file and get ready to write into it.
        '''
        self.output_file = open(output_file_path, 'w')
        # record the current function name within which the code to be translate locates
        self.function_name = 'null'
        self.label_cnter = 0
        self.need_bootstrap = need_bootstrap

        if need_bootstrap:
            self.write_bootstrap()

    def write_bootstrap(self):
        '''
        Write bootstrap code if needed.
        Set SP to 256 and call Sys.init.
        '''
        asm_codes = """// bootstrap codes
        @261
        D=A
        @SP
        M=D

        // call Sys.init 0
        @Sys.init
        0;JMP

        """

        self.output_asmcodes(asm_codes)

    def set_file_name(self, file_name):
        '''
        Inform that the new translation of a new vm file has started.
        '''
        self.file_name = file_name.strip('.vm')

    def output_asmcodes(self, asm_codes):
        asm_codes = '\n'.join([line.strip() for line in asm_codes.split('\n')])
        self.output_file.write(asm_codes)

    def write_arithmetic(self, command: str):
        '''
        Write to the output file the assembly code that implements the given arithmetic-logical command.
        '''
        # add a comment to help to distinguish from which vm command there assembly codes are generated
        asm_codes = '// ' + command

        if command == 'neg' or command == 'not':    # unary operator
            asm_codes += """
            @SP
            M=M-1
            A=M
            D=M
            """
            if command == 'neg':
                asm_codes += 'D=-D \n'
            elif command == 'not':
                asm_codes += 'D=!D \n'
            asm_codes += """
            @SP
            A=M
            M=D

            @SP
            M=M+1
            """
        else:    # binary operator
            asm_codes += """
            @SP
            M=M-1
            A=M
            D=M
            @R13
            M=D

            @SP
            M=M-1
            A=M
            D=M

            @R13
            """

            if command == 'add':
                asm_codes += 'D=D+M'
            elif command == 'sub':
                asm_codes += 'D=D-M'
            elif command == 'and':
                asm_codes += 'D=D&M'
            elif command == 'or':
                asm_codes += 'D=D|M'
            elif command in ('eq', 'gt', 'lt'):
                self.label_cnter += 1
                asm_codes += """D=D-M
                @{OP}_{LABEL}
                D;J{OP}

                D=0
                @STORE_{LABEL}
                0;JMP

                ({OP}_{LABEL})
                D=-1

                (STORE_{LABEL})
                """.format(OP=command.upper(), LABEL=str(self.label_cnter))

            asm_codes += """
                @SP
                A=M
                M=D

                @SP
                M=M+1
                """

        asm_codes += '\n'
        self.output_asmcodes(asm_codes)

    def write_push_pop(self, command_type: C_PUSH or C_POP, segment, index):
        '''
        Write to the output file the assembly code that implements the given push or pop command.
        '''
        asm_codes = ''
        if command_type == C_PUSH:
            # add a comment
            asm_codes += '// push ' + segment + ' ' + index

            # put the number to be pushed into register D
            if segment == 'constant':
                asm_codes += """
                @{i}
                D=A
                """.format(i=index)
            elif segment in ('local', 'argument', 'this', 'that'):
                asm_codes += """
                @{seg}
                D=M
                @{i}
                A=D+A
                D=M
                """.format(seg=seg_hash[segment], i=index)
            elif segment == 'temp':
                asm_codes += """
                @5
                D=A
                @{i}
                A=D+A
                D=M
                """.format(i=index)
            elif segment == 'static':
                label = self.file_name + '.' + index    # label=basement.index
                asm_codes += """
                @{label}
                D=M
                """.format(label=label)
            elif segment == 'pointer':
                asm_codes += """
                @{seg}
                D=M
                """.format(seg=ptr_hash[index])

            # push the number in register D into stack
            asm_codes += """
            @SP
            A=M
            M=D

            @SP
            M=M+1
            """
        elif command_type == C_POP:
            # add a comment
            asm_codes += '// pop ' + segment + ' ' + index

            # pop the number at the top of stack into register D
            asm_codes += """
            @SP
            M=M-1
            A=M
            D=M
            """

            # put the number in register D into segment[index]
            if segment in ('local', 'argument', 'this', 'that'):
                asm_codes += """
                @R13
                M=D

                @{seg}
                D=M
                @{index}
                D=D+A
                @R14
                M=D

                @R13
                D=M
                @R14
                A=M
                M=D
                """.format(seg=seg_hash[segment], index=index)
            elif segment == 'temp':
                asm_codes += """
                @R13
                M=D

                @5
                D=A
                @{i}
                D=D+A
                @R14
                M=D

                @R13
                D=M
                @R14
                A=M
                M=D
                """.format(i=index)
            elif segment == 'static':
                label = self.file_name + '.' + index
                asm_codes += """
                @{label}
                M=D
                """.format(label=label)
            elif segment == 'pointer':
                asm_codes += """
                @{seg}
                M=D
                """.format(seg=ptr_hash[index])

        asm_codes += '\n'
        self.output_asmcodes(asm_codes)

    def write_label(self, label):
        '''
        Write assembly code that effects the label command.
        '''

        asm_codes = """// label {label}
        ({PREFIX}${label})

        """.format(label=label, PREFIX=self.function_name)

        self.output_asmcodes(asm_codes)

    def write_goto(self, label):
        '''
        Write assembly code that effects the goto command.
        '''

        asm_codes = """// goto {label}
        @{PREFIX}${label}
        0;JMP

        """.format(label=label, PREFIX=self.function_name)

        self.output_asmcodes(asm_codes)

    def write_if(self, label):
        '''
        Write assembly code that effects the if-goto command.
        '''

        asm_codes = '''// if-goto {label}
        @SP
        M=M-1
        A=M
        D=M

        @{PREFIX}${label}
        D;JNE

        '''.format(label=label, PREFIX=self.function_name)

        self.output_asmcodes(asm_codes)

    def write_function(self, function_name, n_vars):
        '''
        Write assembly code that effects the function command.
        n_vars: n local variables need to be pushed
        '''

        # (fileName.functionName)
        # repeat n_vars times:
        #    push 0

        self.function_name = function_name

        asm_codes = '''// function {function_name} {n_vars}
        ({function_name})
        @{n_vars}
        D=A
        @R13
        M=D

        ({function_name}$PUSH_LCL_VARS)
        @R13
        D=M
        @{function_name}$END_PUSH_LCL_VARS
        D;JEQ

        @SP
        A=M
        M=0
        @SP
        M=M+1

        @R13
        M=M-1

        @{function_name}$PUSH_LCL_VARS
        0;JMP

        ({function_name}$END_PUSH_LCL_VARS)

        '''.format(function_name=function_name, n_vars=n_vars)

        self.output_asmcodes(asm_codes)

    def write_return(self):
        '''
        Write assembly code that effects the return command.
        '''

        # R13 = retAddr = RAM[LCL-5]
        # ARG[0] = retValue = pop()
        # SP = ARG+1
        # THAT = RAM[LCL-1]
        # THIS = RAM[LCL-2]
        # ARG = RAM[LCL-3]
        # LCL = RAM[LCL-4]
        # goto retAddr

        asm_codes  = '''// return
        @5
        D=A
        @LCL
        A=M
        A=A-D
        D=M
        @R13
        M=D

        @SP
        M=M-1
        A=M
        D=M
        @ARG
        A=M
        M=D

        @ARG
        D=M
        @SP
        M=D+1

        @LCL
        M=M-1
        A=M
        D=M
        @THAT
        M=D

        @LCL
        M=M-1
        A=M
        D=M
        @THIS
        M=D

        @LCL
        M=M-1
        A=M
        D=M
        @ARG
        M=D

        @LCL
        M=M-1
        A=M
        D=M
        @LCL
        M=D

        @R13
        A=M
        0;JMP

        '''

        self.output_asmcodes(asm_codes)

    def write_call(self, function_name, n_args):
        '''
        Write assembly code that effects the call command.
        '''

        # push retAddr
        # push LCL
        # push ARG
        # push THIS
        # push THAT
        # ARG = SP - 5 - n_args
        # LCL = SP
        # goto function_name
        # (function_name$ret.cnter)

        asm_codes = '''// call {function_name} {n_args}
        @{function_name}$ret.{i}
        D=A
        @SP
        A=M
        M=D
        @SP
        M=M+1

        @LCL
        D=M
        @SP
        A=M
        M=D
        @SP
        M=M+1

        @ARG
        D=M
        @SP
        A=M
        M=D
        @SP
        M=M+1

        @THIS
        D=M
        @SP
        A=M
        M=D
        @SP
        M=M+1

        @THAT
        D=M
        @SP
        A=M
        M=D
        @SP
        M=M+1

        @SP
        D=M
        @5
        D=D-A
        @{n_args}
        D=D-A
        @ARG
        M=D

        @SP
        D=M
        @LCL
        M=D

        @{function_name}
        0;JMP

        ({function_name}$ret.{i})

        '''.format(function_name=function_name, n_args=n_args, i=self.label_cnter)

        self.label_cnter += 1
        self.output_asmcodes(asm_codes)

    def close(self):
        '''
        Close the output file.
        '''
        if not self.need_bootstrap:    # single vm file needs a stop loop
            asm_codes = """
            (STOP)
            @STOP
            0;JMP
            """
            self.output_asmcodes(asm_codes)

        self.output_file.close()
