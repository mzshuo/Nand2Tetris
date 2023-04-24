from const import *


class Parser:
    '''
    Parse each VM command into its lexical elements.
    '''

    def __init__(self, input_file):
        '''
        Open the input_file and get ready to parse it.
        '''
        self.vm_file = open(input_file, 'r')
        self.current_command = ''

    def has_more_lines(self):
        '''
        Return True if there has more lines in the input.
        '''
        while True:
            cmd = self.vm_file.readline()
            if cmd == '':
                self.current_command = None
                return False
            
            cmd = cmd.strip('\n').strip()
            if len(cmd) > 1 and cmd[0:2] != '//':
                self.current_command = cmd.split('//')[0]    # remove comments if there are
                return True

    def advance(self):
        '''
        Read the next command from the input and make it the current_command.
        This method should be called only if has_more_command is true.
        Initially there is no current_command.
        '''
        return self.current_command

    def command_type(self):
        '''
        Return a constant representing the type of the current command.
        '''
        args = self.current_command.split(' ')

        if args[0] in arithmetic_commands:
            return C_ARITHMETIC
        elif args[0] == 'push':
            return C_PUSH
        elif args[0] == 'pop':
            return C_POP
        elif args[0] == 'label':
            return  C_LABEL
        elif args[0] == 'goto':
            return C_GOTO
        elif args[0] == 'if-goto':
            return C_IF
        elif args[0] == 'return':
            return C_RETURN
        elif args[0] == 'function':
            return C_FUNCTION
        elif args[0] == 'call':
            return C_CALL

    def arg1(self):
        '''
        Return the first argument of the current command.
        In the case of C_ARITHMETIC, the command itself(add, sub, etc.) is returned.
        Should not be called if the current command if C_RETURN.
        '''
        args = self.current_command.split(' ')
        cmd_type = self.command_type()

        if cmd_type == C_ARITHMETIC:
            return args[0]
        elif cmd_type == C_RETURN:
            raise TypeError
        else:
            return args[1]

    def arg2(self):
        '''
        Return the second argument of the current command.
        Should be called only if the current command is C_PUSH, C_POP, C_FUNCTION or C_CALL.
        '''
        args = self.current_command.split(' ')
        cmd_type = self.command_type()

        if cmd_type == C_PUSH or cmd_type == C_POP or cmd_type == C_FUNCTION or cmd_type == C_CALL:
            return args[2]
        else:
            raise TypeError