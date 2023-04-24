class VMWriter:
    '''
    Writes individual VM commands to the output .vm file.
    '''
    
    def __init__(self, output_file):
        '''
        Creates a new output .vm file and prepares it for writing.
        '''
        self.output_file = open(output_file, 'w')

    def write_push(self, segment, index):
        '''
        Writes a VM push command.
        segment: constant/argument/local/static/this/that/pointer/temp
        '''
        self.output_file.write('push {seg} {i}'.format(seg=segment.value, i=index) + '\n')

    def write_pop(self, segment, index):
        '''
        Writes a VM pop command.
        segment: argument/local/static/local/this/that/pointer/temp
        '''
        self.output_file.write('pop {seg} {i}'.format(seg=segment.value, i=index) + '\n')

    def write_arithmetic(self, command):
        '''
        Writes a VM arithmetic-logical command.
        command: add/sub/neg/eq/gt/lt/and/or/not
        '''
        self.output_file.write(command.value + '\n')

    def write_label(self, label):
        '''
        Writes a VM label command.
        '''
        self.output_file.write('label ' + label + '\n')

    def write_goto(self, label):
        '''
        Writes a VM goto command.
        '''
        self.output_file.write('goto ' + label + '\n')

    def write_if(self, label):
        '''
        Writes a VM if-goto command.
        '''
        self.output_file.write('if-goto ' + label + '\n')

    def write_call(self, function_name, nArgs):
        '''
        Writes a VM call command.
        '''
        self.output_file.write('call {function_name} {nArgs}'.format(function_name=function_name, nArgs=nArgs) + '\n')

    def write_function(self, name, nVars):
        '''
        Writes a VM function command.
        '''
        self.output_file.write('\n' + 'function {name} {nVars}'.format(name=name, nVars=nVars) + '\n')

    def write_return(self):
        '''
        Writes a VM return command.
        '''
        self.output_file.write('return' + '\n')

    def close(self):
        '''
        Closes the output file.
        '''
        self.output_file.close()