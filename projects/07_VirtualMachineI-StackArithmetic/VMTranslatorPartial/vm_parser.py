from const import *
import os


class Parser:
    '''
    Parse each VM command into its lexical elements.
    '''

    def __init__(self, input_file):
        '''
        Open the input_file and get ready to parse it.
        '''
        self.file_name = os.path.basename(input_file).split('.')[0]
        self.vm_commands = []
        self.current_command = -1

        with open(input_file, 'r') as file:
            for cmd in file.readlines():
                cmd = cmd.strip()
                # not a white space nor a comment
                if len(cmd) > 1 and cmd[0:2] != '//':
                    self.vm_commands.append(cmd)

    def has_more_lines(self):
        '''
        Return True if there has more lines in the input.
        '''
        return len(self.vm_commands) > self.current_command + 1

    def advance(self):
        '''
        Read the next command from the input and make it the current_command.
        This method should be called only if has_more_command is true.
        Initially there is no current_command.
        '''
        self.current_command += 1

    def command_type(self):
        '''
        Return a constant representing the type of the current command.
        '''
        command = self.vm_commands[self.current_command]
        args = command.split(' ')

        if args[0] in arithmetic_commands:
            return C_ARITHMETIC
        elif args[0] == 'push':
            return C_PUSH
        elif args[0] == 'pop':
            return C_POP

    def arg1(self):
        '''
        Return the first argument of the current command.
        In the case of C_ARITHMETIC, the command itself(add, sub, etc.) is returned.
        Should not be called if the current command if C_RETURN.
        '''
        command = self.vm_commands[self.current_command]
        args = command.split(' ')
        cmd_type = self.command_type()

        if cmd_type == C_ARITHMETIC:
            return args[0]
        elif cmd_type == C_PUSH or cmd_type == C_POP:
            return args[1]

    def arg2(self):
        '''
        Return the second argument of the current command.
        Should be called only if the current command is C_PUSH, C_POP, C_FUNCTION or C_CALL.
        '''
        command = self.vm_commands[self.current_command]
        args = command.split(' ')
        cmd_type = self.command_type()

        if cmd_type == C_PUSH or cmd_type == C_POP:
            return args[2]
