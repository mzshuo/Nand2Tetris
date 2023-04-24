from const import *
import os


class CodeWriter:
    '''
    Write the assembly code that implements the parsed command.
    '''

    def __init__(self, output_file_path):
        '''
        Open an output file and get ready to write into it.
        '''
        self.file_name = os.path.basename(output_file_path).strip('.asm')
        self.output_file = open(output_file_path, 'w')
        self.cnter = 0

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
                self.cnter += 1
                asm_codes += """D=D-M
                @{OP}_{LABEL}
                D;J{OP}

                D=0
                @STORE_{LABEL}
                0;JMP

                ({OP}_{LABEL})
                D=-1

                (STORE_{LABEL})
                """.format(OP=command.upper(), LABEL=str(self.cnter))

            asm_codes += """
                @SP
                A=M
                M=D

                @SP
                M=M+1
                """

        asm_codes += '\n'
        asm_codes = '\n'.join([line.strip() for line in asm_codes.split('\n')])
        self.output_file.write(asm_codes)

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
        asm_codes = '\n'.join([line.strip() for line in asm_codes.split('\n')])
        self.output_file.write(asm_codes)

    def close(self):
        '''
        Close the output file.
        '''

        asm_codes = """
        (STOP)
        @STOP
        0;JMP
        """
        asm_codes = '\n'.join([line.strip() for line in asm_codes.split('\n')])
        self.output_file.write(asm_codes)
        self.output_file.close()
