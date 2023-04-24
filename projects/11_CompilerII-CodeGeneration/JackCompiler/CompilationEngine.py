import JackTokenizer
import JackLexicon
from JackLexicon import SegmentType
import SymbolTable
import VMWriter


class CompilationEngine:
    '''
    Gets the input from a tokenizer, and emits the output to a .vm output file.
    '''

    def __init__(self, input_file):
        '''
        Creates a new compilation engine with the given input.
        The next method called (by the JackCompiler module) must be compile_class().
        '''

        self.tokenizer = JackTokenizer.JackTokenizer(input_file)
        self.class_symbol_table = SymbolTable.SymbolTable()
        self.subroutine_symbol_table = SymbolTable.SymbolTable()
        self.label_cnter = 0

        output_file = input_file.replace('.jack', '.vm')
        self.vm_writer = VMWriter.VMWriter(output_file)

    def compile_class(self):
        '''
        Compiles a complete class.
        '''

        # Implementation logic: 'class' className '{' class_var_dec* subroutine_dec* '}'

        assert self.tokenizer.advance() == 'class'          # 'class'
        self.class_name = self.tokenizer.advance()          # className
        assert self.tokenizer.advance() == '{'              # '{'

        # class_var_dec*
        while self.tokenizer.has_more_tokens() and self.tokenizer.advance() in ('static', 'field'):
            self.compile_class_var_dec()

        # subroutine_dec*
        while self.tokenizer.token_type() == JackLexicon.TokenType.KEYWORD:
            self.compile_subroutine()

        assert self.tokenizer.symbol() == '}'              # '}'
        self.vm_writer.close()

    def compile_class_var_dec(self):
        '''
        Compiles a static variable declaration, or a field declaration.
        '''

        # Implementation logic: ('static'|'field') type varName (',', varName)* ';'

        kind = self.tokenizer.keyword()
        type = self.tokenizer.advance()
        var_name = self.tokenizer.advance()

        if kind == 'static':
            kind = JackLexicon.VarType.STATIC
        elif kind == 'field':
            kind = JackLexicon.VarType.FIELD
        else:
            raise TypeError

        # Inserts a symbol into the class-level symbol table.
        self.class_symbol_table.define(var_name, type, kind)

        # (',', varName)*
        while self.tokenizer.advance() == ',':
            var_name = self.tokenizer.advance()
            self.class_symbol_table.define(var_name, type, kind)

        assert self.tokenizer.symbol() == ';'       # symbol ';'

    def compile_subroutine(self):
        '''
        Compiles a complete constructor, function or method.
        '''

        # Implementation logic: ('constuctor'|'function'|'method') ('void'|type) subroutineName '(' parameterList ')' subroutineBody
        self.subroutine_symbol_table.reset()

        subroutine_type = self.tokenizer.keyword()    # ('constuctor'|'function'|'method')
        return_type = self.tokenizer.advance()        # ('void'|type)
        subroutine_name = self.tokenizer.advance()    # subroutine_name

        assert self.tokenizer.advance() == '('        # symbol '('

        # Add parameterList
        self.tokenizer.advance()
        self.compile_parameter_list(subroutine_type)

        assert self.tokenizer.symbol() == ')'         # symbol ')'

        # Add subroutineBody
        self.tokenizer.advance()
        self.compile_subroutine_body(subroutine_type, subroutine_name)

    def compile_parameter_list(self, subroutine_type):
        '''
        Compiles a (possibly empty) parameter list.
        Does not handle the enclosing parentheses tokens '(' and ')'.
        '''

        # Implementation logic: ((type varName) (',' type varName)*)?
        if subroutine_type == 'method':
            self.subroutine_symbol_table.define('this', self.class_name, JackLexicon.VarType.ARG)    # arg[0] = this

        while self.tokenizer.symbol() != ')':
            # type
            if self.tokenizer.token_type() == JackLexicon.TokenType.KEYWORD:
                type = self.tokenizer.keyword()
            elif self.tokenizer.token_type() == JackLexicon.TokenType.IDENTIFIER:
                type = self.tokenizer.identifier()

            # varName
            var_name = self.tokenizer.advance()
            assert self.tokenizer.token_type() == JackLexicon.TokenType.IDENTIFIER
            self.subroutine_symbol_table.define(var_name, type, JackLexicon.VarType.ARG)

            # symbol ',' if there is one
            if self.tokenizer.advance() == ',':
                self.tokenizer.advance()

    def compile_subroutine_body(self, subroutine_type, subroutine_name):
        '''
        Compiles a subroutine's body.
        '''

        # Implementation logic: '{' varDec* statements '}'

        # symbol '{'
        assert self.tokenizer.symbol() == '{'       
        self.tokenizer.advance()

        # varDec*
        while self.tokenizer.symbol() == 'var':
            self.compile_var_dec()

        # Writes VM codes.
        nVars = self.subroutine_symbol_table.var_count(JackLexicon.VarType.LCL)
        self.vm_writer.write_function(self.class_name+'.'+subroutine_name, nVars)

        if subroutine_type == 'constructor':
            field_num = self.class_symbol_table.var_count(JackLexicon.VarType.FIELD)
            self.vm_writer.write_push(SegmentType.CONSTANT, field_num)
            self.vm_writer.write_call('Memory.alloc', 1)
            self.vm_writer.write_pop(SegmentType.POINTER, 0)
        elif subroutine_type == 'method':
            self.vm_writer.write_push(SegmentType.ARGUMENT, 0)
            self.vm_writer.write_pop(SegmentType.POINTER, 0)

        # statements
        self.compile_statements()

        # symbol '}'
        assert self.tokenizer.symbol() == '}'
        self.tokenizer.advance()

    def compile_var_dec(self):
        '''
        Compiles a variable declaration.
        '''

        # Implementation logic: 'var' type varName (',' varName)* ';'
        assert self.tokenizer.keyword() == 'var'        # 'var'
        type = self.tokenizer.advance()                 # type

        # Add varName (',' varName)*
        while True:
            var_name = self.tokenizer.advance()
            self.subroutine_symbol_table.define(var_name, type, JackLexicon.VarType.LCL)

            if self.tokenizer.advance() == ';':
                break
            else:
                assert self.tokenizer.symbol() == ','

        # Add symbol ';'
        assert self.tokenizer.symbol() == ';'
        self.tokenizer.advance()

    def compile_statements(self):
        '''
        Compiles a sequence of statements.
        Does not handle of enclosing curly bracket tokens '{' and '}'.
        '''
        # Implementation logic: (letStatement|ifStatement|doStatement|whileStatement|returnStatement)*

        while self.tokenizer.token_type() == JackLexicon.TokenType.KEYWORD:
            if self.tokenizer.keyword() == 'let':
                self.compile_let()
            elif self.tokenizer.keyword() == 'if':
                self.compile_if()
            elif self.tokenizer.keyword() == 'do':
                self.compile_do()
            elif self.tokenizer.keyword() == 'while':
                self.compile_while()
            elif self.tokenizer.keyword() == 'return':
                self.compile_return()
            
    def compile_let(self):
        '''
        Compiles a let statement.
        '''
        # Implementation logic: 'let' varName ('[' expression ']')? '=' expression ';'

        assert self.tokenizer.keyword() == 'let'        # 'let'
        var_name = self.tokenizer.advance()             # varName
        is_array = False

        # assure the segment and index of var_name
        kind, index = self.findVariable(var_name)
        segment = self.kind2segment(kind)

        # if var is an array
        if self.tokenizer.advance() == '[':
            is_array = True
            self.tokenizer.advance()                # symbol '['
            self.compile_expression()               # expression -> offset from the base address
            assert self.tokenizer.symbol() == ']'   # symbol ']'
            self.tokenizer.advance()

            # push offset (by compile_expression)
            # push var_name
            # add
            self.vm_writer.write_push(segment, index)
            self.vm_writer.write_arithmetic(JackLexicon.CommandType.ADD)
        
        assert self.tokenizer.symbol() == '='       # '='
        self.tokenizer.advance()
        self.compile_expression()                   # expression
        assert self.tokenizer.symbol() == ';'       # symbol ';'
        self.tokenizer.advance()

        # Writes VM codes.
        if is_array:
            self.vm_writer.write_pop(SegmentType.TEMP, 0)
            self.vm_writer.write_pop(SegmentType.POINTER, 1)
            self.vm_writer.write_push(SegmentType.TEMP, 0)
            self.vm_writer.write_pop(SegmentType.THAT, 0)
        else:
            self.vm_writer.write_pop(segment, index)

    def compile_if(self):
        '''
        Compiles an if statement, possibly with a trailing else clause.
        '''

        # Implementation logic: 'if' '(' expression ')' '{' statements '}' ('else' '{' statements '}')?

        # 'if' '(' expression ')'
        assert self.tokenizer.keyword() == 'if'  
        assert self.tokenizer.advance() == '('   
        self.tokenizer.advance()                
        self.compile_expression()
        assert self.tokenizer.symbol() == ')' 

        else_label = 'ELSE_' + str(self.label_cnter)
        end_label = 'END_' + str(self.label_cnter)
        self.label_cnter += 1

        # Writes if-goto
        self.vm_writer.write_arithmetic(JackLexicon.CommandType.NOT)
        self.vm_writer.write_if(else_label)

        assert self.tokenizer.advance() == '{'      # '{'
        self.tokenizer.advance()                    # statements1
        self.compile_statements()
        assert self.tokenizer.symbol() == '}'       # '}'
        self.tokenizer.advance()

        # Writes label
        self.vm_writer.write_goto(end_label)
        self.vm_writer.write_label(else_label)

        if self.tokenizer.keyword() == 'else':
            assert self.tokenizer.advance() == '{'  # symbol '{'
            self.tokenizer.advance()                # statements2
            self.compile_statements()
            assert self.tokenizer.symbol() == '}'   # symbol '}'
            self.tokenizer.advance()

        # Writes label
        self.vm_writer.write_label(end_label)

    def compile_do(self):
        '''
        Compiles a do statement.
        '''

        # Implementation logic: 'do' subroutineCall ';'
        assert self.tokenizer.keyword() == 'do' 

        '''
        subroutineCall: subroutineName '(' expressionList ')' 
                        | (className|varName) '.' subroutineName '(' expressionList ')'
        '''
        # identifier xxxName
        name = self.tokenizer.advance()
        dot = self.tokenizer.advance()
        if self.subroutine_symbol_table.find(name):
            class_name = self.subroutine_symbol_table.type_of(name)
            kind = self.subroutine_symbol_table.kind_of(name)
            segment = self.kind2segment(kind)
            index = self.subroutine_symbol_table.index_of(name)
            type = 'method'
        elif self.class_symbol_table.find(name):
            class_name = self.class_symbol_table.type_of(name)
            kind = self.class_symbol_table.kind_of(name)
            segment = self.kind2segment(kind)
            index = self.class_symbol_table.index_of(name)
            type = 'method'
        elif dot != '.':
            segment = SegmentType.POINTER
            index = 0
            type = 'method'
        else:
            type = 'function'       # if there is no '.' after, it is a method.

        # push this[0] as arg[0]
        plus1 = 0
        if type == 'method':
            self.vm_writer.write_push(segment, index)
            plus1 = 1

        # figure out function name
        if self.tokenizer.symbol() == '.':
            subroutine_name = self.tokenizer.advance()
            self.tokenizer.advance()
            
            if type == 'method':
                function_name = class_name + '.' + subroutine_name
            else:
                function_name = name + '.' + subroutine_name
        else:
            function_name = self.class_name + '.' + name

        assert self.tokenizer.symbol() == '('   # symbol '('
        self.tokenizer.advance()                # expressionList
        nArgs = self.compile_expression_list()
        assert self.tokenizer.symbol() == ')'   # symbol ')'
        self.tokenizer.advance()
        assert self.tokenizer.symbol() == ';'   # symbol ';'
        self.tokenizer.advance()

        self.vm_writer.write_call(function_name, nArgs+plus1)
        self.vm_writer.write_pop(SegmentType.TEMP, 0)

    def compile_while(self):
        '''
        Compiles a while statement.
        '''

        # Implementation logic: 'while' '(' expression ')' '{' statements '}'
        assert self.tokenizer.keyword() == 'while'
        begin_label = 'BEGIN_' + str(self.label_cnter)
        end_label = 'END_' + str(self.label_cnter)
        self.label_cnter += 1

        # (BEGIN)
        self.vm_writer.write_label(begin_label)

        # expression
        assert self.tokenizer.advance() == '('
        self.tokenizer.advance()
        self.compile_expression()
        assert self.tokenizer.symbol() == ')'

        # if not expression: goto END
        self.vm_writer.write_arithmetic(JackLexicon.CommandType.NOT)
        self.vm_writer.write_if(end_label)

        # statements
        assert self.tokenizer.advance() == '{'
        self.tokenizer.advance()
        self.compile_statements()
        assert self.tokenizer.symbol() == '}'
        self.tokenizer.advance()

        # goto BEGIN
        # (END)
        self.vm_writer.write_goto(begin_label)
        self.vm_writer.write_label(end_label)

    def compile_return(self):
        '''
        Compiles a return statement.
        '''
        # Implementation logic: 'return' expression? ';'
        assert self.tokenizer.keyword() == 'return'

        # expression
        if self.tokenizer.advance() != ';':
            self.compile_expression()
        else:
            self.vm_writer.write_push(SegmentType.CONSTANT, 0)

        # ';'
        assert self.tokenizer.symbol() == ';'
        self.tokenizer.advance()
        self.vm_writer.write_return()

    def compile_expression(self):
        '''
        Compiles an expression.
        '''
        # Implementation logic: term (op term)*

        # Add term
        self.compile_term()

        # Add (op term)*
        while self.tokenizer.symbol() in JackLexicon.op:
            op = self.tokenizer.symbol()
            self.tokenizer.advance()
            self.compile_term()

            if op == '+':
                self.vm_writer.write_arithmetic(JackLexicon.CommandType.ADD)
            elif op == '-':
                self.vm_writer.write_arithmetic(JackLexicon.CommandType.SUB)
            elif op == '*':
                self.vm_writer.write_call('Math.multiply', 2)
            elif op == '/':
                self.vm_writer.write_call('Math.divide', 2)
            elif op == '&':
                self.vm_writer.write_arithmetic(JackLexicon.CommandType.AND)
            elif op == '|':
                self.vm_writer.write_arithmetic(JackLexicon.CommandType.OR)
            elif op == '>':
                self.vm_writer.write_arithmetic(JackLexicon.CommandType.GT)
            elif op == '<':
                self.vm_writer.write_arithmetic(JackLexicon.CommandType.LT)
            elif op == '=':
                self.vm_writer.write_arithmetic(JackLexicon.CommandType.EQ)

    def compile_term(self):
        '''
        Compiles a term.
        If the current token is an identifier, this method resolves it into a variable, an array entry, or a subroutine call.
        '''

        '''
        Implementation logic: integerConstant|stringConstant|keywordConstant|varName|
                              varName'['expression']' | subroutineCall | '('expression')' | unaryOp term
        subroutineCall: subroutineName '(' expressionList ')' 
                        | (className|varName) '.' subroutineName '(' expressionList ')'
        '''

        # term =  '('expression')'
        if self.tokenizer.symbol() == '(':
            self.tokenizer.advance()
            self.compile_expression()
            assert self.tokenizer.symbol() == ')'
            self.tokenizer.advance()
        # term = unaryOp term
        elif self.tokenizer.symbol() in JackLexicon.unaryOp:
            op = self.tokenizer.symbol()
            self.tokenizer.advance()
            self.compile_term()
            if op == '-':
                self.vm_writer.write_arithmetic(JackLexicon.CommandType.NEG)
            elif op == '~':
                self.vm_writer.write_arithmetic(JackLexicon.CommandType.NOT)
        # term = integerConstant
        elif self.tokenizer.token_type() == JackLexicon.TokenType.INT_CONST:
            num = self.tokenizer.int_value()
            self.tokenizer.advance()
            self.vm_writer.write_push(SegmentType.CONSTANT, num)
        # term = stringConstant
        elif self.tokenizer.token_type() == JackLexicon.TokenType.STRING_CONST:
            string = self.tokenizer.string_value()
            self.tokenizer.advance()
            # string = String.new(len)
            self.vm_writer.write_push(SegmentType.CONSTANT, len(string))
            self.vm_writer.write_call('String.new', 1)
            # set string[i] = char[i]
            for i in range(len(string)):
                self.vm_writer.write_push(SegmentType.CONSTANT, ord(string[i]))
                self.vm_writer.write_call('String.appendChar', 2)
        # term = keywordConstant
        elif self.tokenizer.token_type() == JackLexicon.TokenType.KEYWORD:
            keyword = self.tokenizer.keyword()
            self.tokenizer.advance()
            if keyword == 'true':
                self.vm_writer.write_push(SegmentType.CONSTANT, 1)
                self.vm_writer.write_arithmetic(JackLexicon.CommandType.NEG)
            elif keyword in ('false', 'null'):
                self.vm_writer.write_push(SegmentType.CONSTANT, 0)
            elif keyword == 'this':
                self.vm_writer.write_push(SegmentType.POINTER, 0)
        # term = varName | varName'['expression']' | subroutineName '(' expressionList ')'
        #                | (className|varName) '.' subroutineName '(' expressionList ')'
        else:
            assert self.tokenizer.token_type() == JackLexicon.TokenType.IDENTIFIER
            name = self.tokenizer.identifier()
            next = self.tokenizer.advance()

            # term = varName'['expression']'
            if next == '[':
                self.tokenizer.advance()
                self.compile_expression()                                       # offset
                assert self.tokenizer.symbol() == ']'
                self.tokenizer.advance()

                if self.subroutine_symbol_table.find(name):
                    kind = self.subroutine_symbol_table.kind_of(name)
                    index = self.subroutine_symbol_table.index_of(name)
                elif self.class_symbol_table.find(name):
                    kind = self.class_symbol_table.kind_of(name)
                    index = self.class_symbol_table.index_of(name)
                segment = self.kind2segment(kind)
                self.vm_writer.write_push(segment, index)                       # base address
                self.vm_writer.write_arithmetic(JackLexicon.CommandType.ADD)
                self.vm_writer.write_pop(SegmentType.POINTER, 1)
                self.vm_writer.write_push(SegmentType.THAT, 0)
            # term = subroutineName '(' expressionList ')'
            elif next == '(':
                self.tokenizer.advance()

                self.vm_writer.write_push(SegmentType.POINTER, 0)
                nArgs = self.compile_expression_list()
                self.vm_writer.write_call(self.class_name+'.'+name, nArgs+1)

                assert self.tokenizer.symbol() == ')'
                self.tokenizer.advance()
            # term = (className|varName) '.' subroutineName '(' expressionList ')'
            elif next == '.':
                if self.subroutine_symbol_table.find(name):
                    type = 'method'
                    kind = self.subroutine_symbol_table.kind_of(name)
                    segment = self.kind2segment(kind)
                    index = self.subroutine_symbol_table.index_of(name)
                    name = self.subroutine_symbol_table.type_of(name)
                elif self.class_symbol_table.find(name):
                    type = 'method'
                    kind = self.class_symbol_table.kind_of(name)
                    segment = self.kind2segment(kind)
                    index = self.class_symbol_table.index_of(name)
                    name = self.class_symbol_table.type_of(name)
                else:
                    type = 'function'

                if type == 'method':
                    self.vm_writer.write_push(segment, index)
                    plus1 = 1
                else:
                    plus1 = 0

                subroutine_name = self.tokenizer.advance()
                assert self.tokenizer.advance() == '('
                self.tokenizer.advance()
                nArgs = self.compile_expression_list()
                assert self.tokenizer.symbol() == ')'
                self.tokenizer.advance()

                self.vm_writer.write_call(name+'.'+subroutine_name, nArgs+plus1)
            # term = varName
            else:
                kind, index = self.findVariable(name)
                segment = self.kind2segment(kind)
                self.vm_writer.write_push(segment, index)

    def compile_expression_list(self):
        '''
        Compiles a (possibly empty) comma-seperated list of expressions.
        Returns the number of expressions in the list.
        '''
        # Implementation logic: (expression (',' expression)* )?
        nArgs = 0

        if self.tokenizer.symbol() != ')':
            self.compile_expression()
            nArgs += 1

            while self.tokenizer.symbol() != ')':    # as expressionList only exists like '(' expressionList ')'
                assert self.tokenizer.symbol() == ','
                self.tokenizer.advance()
                self.compile_expression()
                nArgs += 1

        return nArgs

    def kind2segment(self, kind):
        '''
        Converts a kind type into a segment type.
        '''
        if kind == JackLexicon.VarType.ARG:
            segment = SegmentType.ARGUMENT
        elif kind == JackLexicon.VarType.LCL:
            segment = SegmentType.LOCAL
        elif kind == JackLexicon.VarType.STATIC:
            segment = SegmentType.STATIC
        elif kind == JackLexicon.VarType.FIELD:
            segment = SegmentType.THIS
        return segment

    def findVariable(self, var_name):
        '''
        Finds var_name in subroutine symbol table and class symbol table.
        Returns the corresponding kind and index.
        '''
        if self.subroutine_symbol_table.find(var_name):
            kind = self.subroutine_symbol_table.kind_of(var_name)
            index = self.subroutine_symbol_table.index_of(var_name)
        elif self.class_symbol_table.find(var_name):
            kind = self.class_symbol_table.kind_of(var_name)
            index = self.class_symbol_table.index_of(var_name)
        else:
            return False
        
        return (kind, index)