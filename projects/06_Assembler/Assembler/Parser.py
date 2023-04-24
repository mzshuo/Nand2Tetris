'''
This module is to help encapsulate access to the input code. 
'''


class Parser:
    '''
    Reads an assembly language command, parses it, and provides convenient access to the command’s components(fields and symbols). 
    In addition, removes all white space and comments.
    '''

    def __init__(self, file_path):
        '''
        This is a function to open the input file/stream and get ready to parse it
        :param file_path: the path of the asm file to be processed
        '''
        self.asm_codes = []
        self.current_command = -1

        with open(file_path, 'r') as file:
            texts = file.read().split('\n')

        # remove all white space and comments
        for line in texts:
            line = line.strip()
            if len(line) > 0 and line[0] != '/':    # this line is a command rather than a blank line or a commment
                command = line.split('//')[0]    # remove the comment if there is one
                self.asm_codes.append(command)

    def hasMoreCommands(self):
        '''
        This function is to analyze if there are more commands in the input
        :return: True if there are more commands in the input
        '''
        return self.current_command + 1 < len(self.asm_codes)

    def advance(self):
        '''
        This function is to read the next command from the input and make it the current command.
        '''
        self.current_command += 1

    def restart(self):
        '''
        This function is to restart the parser from the first command.
        '''
        self.current_command = -1

    def commandType(self):
        '''
        This function is to return the type of the current command
        :return: 'A_COMMAND' for an A-instruction like @xxx
                 'C_COMMAND' for a C-instruction like dest=comp;jump
                 'L_COMMAND' for a pseudo-command like (xxx)
        '''
        first_char = self.asm_codes[self.current_command][0]
        if first_char == '@':
            return 'A_COMMAND'
        elif first_char == '(':
            return 'L_COMMAND'
        else:
            return 'C_COMMAND'

    def symbol(self):
        '''
        This function is to return the symbol of decimal xxx of the current command.
        It should be called only when commandType() is 'A_COMMAND' or 'L_COMMAND'.
        :return: the symbol part of an A-instrction or a label command
        '''
        command = self.asm_codes[self.current_command]
        if self.commandType() == 'A_COMMAND':    # @xxx
            return command[1:]
        elif self.commandType() == 'L_COMMAND':    # (xxx)
            return command[1:-1]
        else:
            return False

    def dest(self):
        '''
        This function is to return the dest mnenomic in the current C command (dest=comp;jump)
        :return: the dest part of a C-instruction
        '''
        command = self.asm_codes[self.current_command]
        idx = command.find('=')
        if idx == -1:
            dst = ''
        else:
            dst = command[0: idx].strip()
        return dst

    def comp(self):
        '''
        This function is to return the comp mnenomic in the current C command (dest=comp;jump)
        :return: the comp part of a C-instruction
        '''
        command = self.asm_codes[self.current_command]
        idx1 = command.find('=')
        idx2 = command.find(';')
        if idx2 == -1:
            cmp = command[idx1+1:]
        else:
            cmp = command[idx1+1: idx2]

        cmp = cmp.strip()
        return cmp

    def jump(self):
        '''
        This function is to return the jump mnenomic in the current C command (dest=comp;jump)
        :return: the jump part of a C-instruction
        '''
        command = self.asm_codes[self.current_command]
        idx = command.find(';')
        if idx == -1:
            jmp = ''
        else:
            jmp = command[idx+1:].strip()
        return jmp
