import JackTokenizer
import JackLexicon
import xml.etree.ElementTree as ET


class CompilationEngine:
    '''
    Get the input from a tokenizer, and emit the output to an output file.
    '''

    def __init__(self, input_file):
        '''
        Create a new compilation engine with the given input and output.
        The next method called (by the JackAnalyzer module) must be compile_class().
        '''
        self.tokenizer = JackTokenizer.JackTokenizer(input_file)
        self.output_file = input_file.replace('.jack', '.xml')

    def compile_class(self):
        '''
        Compile a complete class.
        '''

        # Implementation logic: 'class' className '{' class_var_dec* subroutine_dec* '}'
        root = ET.Element('class')

        # Add keyword 'class'.
        token = self.tokenizer.advance()
        assert token == 'class'
        node = ET.SubElement(root, 'keyword')
        node.text = self.tokenizer.keyword()

        # Add identifier className
        token = self.tokenizer.advance()
        assert self.tokenizer.token_type() == JackLexicon.IDENTIFIER
        node = ET.SubElement(root, 'identifier')
        node.text = self.tokenizer.identifier()

        # Add symbol '{'
        token = self.tokenizer.advance()
        assert token == '{'
        node = ET.SubElement(root, 'symbol')
        node.text = self.tokenizer.symbol()

        # Add class_var_dec*
        while self.tokenizer.has_more_tokens() and self.tokenizer.advance() in ('static', 'field'):
            self.compile_class_var_dec(root)

        # Add subroutine_dec*
        while self.tokenizer.token_type() == JackLexicon.KEYWORD:
            self.compile_subroutine(root)

        # Add symbol '}'
        assert self.tokenizer.symbol() == '}'
        node = ET.SubElement(root, 'symbol')
        node.text = self.tokenizer.symbol()

        tree = ET.ElementTree(root)
        ET.indent(tree)
        tree.write(self.output_file)

    def compile_class_var_dec(self, root):
        '''
        Compile a static variable declaration, or a field declaration.
        '''
        # Implementation logic: ('static'|'field') type varName (',', varName)* ';'
        subroot = ET.SubElement(root, 'classVarDec')

        # Add keyword 'static' or 'field'
        assert self.tokenizer.keyword() in ('static', 'field')
        node = ET.SubElement(subroot, 'keyword')
        node.text = self.tokenizer.keyword()

        # Add type ('int'|'boolean'|'char'|className)
        type = self.tokenizer.advance()
        tag = ''
        if type in JackLexicon.keyword:
            tag = 'keyword'
        else:
            tag = 'identifier'
        node = ET.SubElement(subroot, tag)
        node.text = type

        # Add identifier varName
        varName = self.tokenizer.advance()
        node = ET.SubElement(subroot, 'identifier')
        node.text = varName

        # Add (',', varName)*
        while self.tokenizer.advance() == ',':
            node = ET.SubElement(subroot, 'symbol')
            node.text = self.tokenizer.symbol()
            node = ET.SubElement(subroot, 'identifier')
            node.text = self.tokenizer.advance()

        # Add symbol ';'
        assert self.tokenizer.symbol() == ';'
        node = ET.SubElement(subroot, 'symbol')
        node.text = self.tokenizer.symbol()

    def compile_subroutine(self, root):
        '''
        Compile a complete constructor, function or method.
        '''
        # Implementation logic: ('constuctor'|'function'|'method') ('void'|type) subroutineName '(' parameterList ')' subroutineBody
        subroot = ET.SubElement(root, 'subroutineDec')

        # Add keyword ('constuctor'|'function'|'method')
        assert self.tokenizer.keyword() in ('constructor', 'function', 'method')
        node = ET.SubElement(subroot, 'keyword')
        node.text = self.tokenizer.keyword()

        # Add keyword or identifier ('void'|type)
        token = self.tokenizer.advance()
        tag = ''
        if token in JackLexicon.keyword:
            tag = 'keyword'
        else:
            tag = 'identifier'
        node = ET.SubElement(subroot, tag)
        node.text = token

        # Add identifier subroutineName
        token = self.tokenizer.advance()
        assert self.tokenizer.token_type() == JackLexicon.IDENTIFIER
        node = ET.SubElement(subroot, 'identifier')
        node.text = token

        # Add symbol '('
        assert self.tokenizer.advance() == '('
        node = ET.SubElement(subroot, 'symbol')
        node.text = self.tokenizer.symbol()

        # Add parameterList
        self.tokenizer.advance()
        self.compile_parameter_list(subroot)

        # Add symbol ')'
        assert self.tokenizer.symbol() == ')'
        node = ET.SubElement(subroot, 'symbol')
        node.text = self.tokenizer.symbol()

        # Add subroutineBody
        self.tokenizer.advance()
        self.compile_subroutine_body(subroot)

    def compile_parameter_list(self, root):
        '''
        Compile a (possibly empty) parameter list.
        Does not handle the enclosing parentheses tokens '(' and ')'.
        '''
        # Implementation logic: ((type varName) (',' type varName)*)?
        subroot = ET.SubElement(root, 'parameterList')
        subroot.text = '\n\t\t'    # prevent subroot becoming a null node

        while self.tokenizer.symbol() != ')':
            # Add type
            if self.tokenizer.token_type() == JackLexicon.KEYWORD:
                node = ET.SubElement(subroot, 'keyword')
                node.text = self.tokenizer.keyword()
            elif self.tokenizer.token_type() == JackLexicon.IDENTIFIER:
                node = ET.SubElement(subroot, 'identifier')
                node.text = self.tokenizer.identifier()

            # Add varName
            token = self.tokenizer.advance()
            assert self.tokenizer.token_type() == JackLexicon.IDENTIFIER
            node = ET.SubElement(subroot, 'identifier')
            node.text = token

            # Add symbol ',' if there is one
            if self.tokenizer.advance() == ',':
                node = ET.SubElement(subroot, 'symbol')
                node.text = self.tokenizer.symbol()
                self.tokenizer.advance()

    def compile_subroutine_body(self, root):
        '''
        Compile a subroutine's body.
        '''
        # Implementation logic: '{' varDec* statements '}'
        subroot = ET.SubElement(root, 'subroutineBody')

        # Add symbol '{'
        assert self.tokenizer.symbol() == '{'
        node = ET.SubElement(subroot, 'symbol')
        node.text = self.tokenizer.symbol()
        self.tokenizer.advance()

        # Add varDec*
        while self.tokenizer.symbol() == 'var':
            self.compile_var_dec(subroot)
        
        # Add statements
        self.compile_statements(subroot)

        # Add symbol '}'
        assert self.tokenizer.symbol() == '}'
        node = ET.SubElement(subroot, 'symbol')
        node.text = self.tokenizer.symbol()
        self.tokenizer.advance()

    def compile_var_dec(self, root):
        '''
        Compile a variable declaration.
        '''
        # Implementation logic: 'var' type varName (',' varName)* ';'
        subroot = ET.SubElement(root, 'varDec')

        # Add keyword 'var'
        assert self.tokenizer.keyword() == 'var'
        node = ET.SubElement(subroot, 'keyword')
        node.text = self.tokenizer.keyword()

        # Add keyword of identifier type
        token = self.tokenizer.advance()
        if token in JackLexicon.keyword:
            node = ET.SubElement(subroot, 'keyword')
            node.text = self.tokenizer.keyword()
        else:
            node = ET.SubElement(subroot, 'identifier')
            node.text = self.tokenizer.identifier()

        # Add varName (',' varName)*
        while True:
            node = ET.SubElement(subroot, 'identifier')
            node.text = self.tokenizer.advance()

            if self.tokenizer.advance() == ';':
                break

            assert self.tokenizer.symbol() == ','
            node = ET.SubElement(subroot, 'symbol')
            node.text = self.tokenizer.symbol()

        # Add symbol ';'
        node = ET.SubElement(subroot, 'symbol')
        node.text = self.tokenizer.symbol()
        self.tokenizer.advance()

    def compile_statements(self, root):
        '''
        Compile a sequence of statements.
        Does not handle of enclosing curly bracket tokens '{' and '}'.
        '''
        # Implementation logic: (letStatement|ifStatement|doStatement|whileStatement|returnStatement)*
        subroot = ET.SubElement(root, 'statements')
        subroot.text = '\n\t\t'    # prevent the node from being a null node

        while self.tokenizer.token_type() == JackLexicon.KEYWORD:
            if self.tokenizer.keyword() == 'let':
                self.compile_let(subroot)
            elif self.tokenizer.keyword() == 'if':
                self.compile_if(subroot)
            elif self.tokenizer.keyword() == 'do':
                self.compile_do(subroot)
            elif self.tokenizer.keyword() == 'while':
                self.compile_while(subroot)
            elif self.tokenizer.keyword() == 'return':
                self.compile_return(subroot)
            assert True, 'The token is expeced to be one the above five types.'

    def compile_let(self, root):
        '''
        Compile a let statement.
        '''
        # Implementation logic: 'let' varName ('[' expression ']')? '=' expression ';'
        subroot = ET.SubElement(root, 'letStatement')

        # Add keyword 'let'
        assert self.tokenizer.keyword() == 'let'
        node = ET.SubElement(subroot, 'keyword')
        node.text = self.tokenizer.keyword()

        # Add identifier varName
        token = self.tokenizer.advance()
        assert self.tokenizer.token_type() == JackLexicon.IDENTIFIER
        node = ET.SubElement(subroot, 'identifier')
        node.text = token

        if self.tokenizer.advance() == '[':
            # Add symbol '['
            node = ET.SubElement(subroot, 'symbol')
            node.text = self.tokenizer.symbol()
            self.tokenizer.advance()

            # Add expression
            self.compile_expression(subroot)

            # Add symbol ']'
            assert self.tokenizer.symbol() == ']'
            node = ET.SubElement(subroot, 'symbol')
            node.text = self.tokenizer.symbol()
            self.tokenizer.advance()

        # Add symbol '='
        assert self.tokenizer.symbol() == '='
        node = ET.SubElement(subroot, 'symbol')
        node.text = self.tokenizer.symbol()
        self.tokenizer.advance()

        # Add expression
        self.compile_expression(subroot)

        # Add symbol ';'
        assert self.tokenizer.symbol() == ';'
        node = ET.SubElement(subroot, 'symbol')
        node.text = self.tokenizer.symbol()
        self.tokenizer.advance()

    def compile_if(self, root):
        '''
        Compile an if statement, possibly with a trailing else clause.
        '''
        # Implementation logic: 'if' '(' expression ')' '{' statements '}' ('else' '{' statements '}')?
        subroot = ET.SubElement(root, 'ifStatement')

        # Add keyword 'if'
        assert self.tokenizer.keyword() == 'if'
        node = ET.SubElement(subroot, 'keyword')
        node.text = self.tokenizer.keyword()

        # Add symbol '('
        assert self.tokenizer.advance() == '('
        node = ET.SubElement(subroot, 'symbol')
        node.text = self.tokenizer.symbol()

        # Add expression
        self.tokenizer.advance()
        self.compile_expression(subroot)

        # Add symbol ')'
        assert self.tokenizer.symbol() == ')'
        node = ET.SubElement(subroot, 'symbol')
        node.text = self.tokenizer.symbol()

        # Add symbol '{'
        assert self.tokenizer.advance() == '{'
        node = ET.SubElement(subroot, 'symbol')
        node.text = self.tokenizer.symbol()

        # Add statements
        self.tokenizer.advance()
        self.compile_statements(subroot)

        # Add symbol '}'
        assert self.tokenizer.symbol() == '}'
        node = ET.SubElement(subroot, 'symbol')
        node.text = self.tokenizer.symbol()
        self.tokenizer.advance()

        if self.tokenizer.keyword() == 'else':
            # Add keyword 'else'
            node = ET.SubElement(subroot, 'keyword')
            node.text = self.tokenizer.keyword()

            # Add symbol '{'
            assert self.tokenizer.advance() == '{'
            node = ET.SubElement(subroot, 'symbol')
            node.text = self.tokenizer.symbol()

            # Add statements
            self.tokenizer.advance()
            self.compile_statements(subroot)

            # Add symbol '}'
            assert self.tokenizer.symbol() == '}'
            node = ET.SubElement(subroot, 'symbol')
            node.text = self.tokenizer.symbol()
            self.tokenizer.advance()

    def compile_do(self, root):
        '''
        Compile a do statement.
        '''
        # Implementation logic: 'do' subroutineCall ';'
        subroot = ET.SubElement(root, 'doStatement')

        # Add keyword 'do'
        assert self.tokenizer.keyword() == 'do'
        node = ET.SubElement(subroot, 'keyword')
        node.text = self.tokenizer.keyword()

        '''
        Add subroutineCall
        subroutineCall: subroutineName '(' expressionList ')' 
                        | (className|varName) '.' subroutineName '(' expressionList ')'
        '''
        # Add identifier xxxName
        name = self.tokenizer.advance()
        node = ET.SubElement(subroot, 'identifier')
        node.text = name

        if self.tokenizer.advance() == '.':
            # Add symbol '.' if there is one
            node = ET.SubElement(subroot, 'symbol')
            node.text = self.tokenizer.symbol()

            # Add identifier subroutineName
            name = self.tokenizer.advance()
            node = ET.SubElement(subroot, 'identifier')
            node.text = name
            self.tokenizer.advance()

        # Add symbol '('
        assert self.tokenizer.symbol() == '('
        node = ET.SubElement(subroot, 'symbol')
        node.text = self.tokenizer.symbol()
        
        # Add expressionList
        self.tokenizer.advance()
        self.compile_expression_list(subroot)

        # Add symbol ')'
        assert self.tokenizer.symbol() == ')'
        node = ET.SubElement(subroot, 'symbol')
        node.text = self.tokenizer.symbol()
        self.tokenizer.advance()

        # Add symbol ';'
        assert self.tokenizer.symbol() == ';'
        node = ET.SubElement(subroot, 'symbol')
        node.text = self.tokenizer.symbol()
        self.tokenizer.advance()

    def compile_while(self, root):
        '''
        Compile a while statement.
        '''
        # Implementation logic: 'while' '(' expression ')' '{' statements '}'
        subroot = ET.SubElement(root, 'whileStatement')

        # Add keyword 'while'
        assert self.tokenizer.keyword() == 'while'
        node = ET.SubElement(subroot, 'keyword')
        node.text = self.tokenizer.keyword()

        # Add symbol '('
        assert self.tokenizer.advance() == '('
        node = ET.SubElement(subroot, 'symbol')
        node.text = self.tokenizer.symbol()

        # Add expression
        self.tokenizer.advance()
        self.compile_expression(subroot)

        # Add symbol ')'
        assert self.tokenizer.symbol() == ')'
        node = ET.SubElement(subroot, 'symbol')
        node.text = self.tokenizer.symbol()

        # Add symbol '{'
        assert self.tokenizer.advance() == '{'
        node = ET.SubElement(subroot, 'symbol')
        node.text = self.tokenizer.symbol()

        # Add statements
        self.tokenizer.advance()
        self.compile_statements(subroot)

        # Add symbol '}'
        assert self.tokenizer.symbol() == '}'
        node = ET.SubElement(subroot, 'symbol')
        node.text = self.tokenizer.symbol()
        self.tokenizer.advance()

    def compile_return(self, root):
        '''
        Compile a return statement.
        '''
        # Implementation logic: 'return' expression? ';'
        subroot = ET.SubElement(root, 'returnStatement')

        # Add keyword 'return'
        assert self.tokenizer.keyword() == 'return'
        node = ET.SubElement(subroot, 'keyword')
        node.text = self.tokenizer.keyword()

        # Add expression
        if self.tokenizer.advance() != ';':
            self.compile_expression(subroot)

        # Add symbol ';'
        assert self.tokenizer.symbol() == ';'
        node = ET.SubElement(subroot, 'symbol')
        node.text = self.tokenizer.symbol()
        self.tokenizer.advance()

    def compile_expression(self, root):
        '''
        Compile an expression.
        '''
        # Implementation logic: term (op term)*
        subroot = ET.SubElement(root, 'expression')

        # Add term
        self.compile_term(subroot)

        # Add (op term)*
        while self.tokenizer.symbol() in JackLexicon.op:
            # Add op
            node = ET.SubElement(subroot, 'symbol')
            node.text = self.tokenizer.symbol()
            # Add term
            self.tokenizer.advance()
            self.compile_term(subroot)

    def compile_term(self, root):
        '''
        Compile a term.
        If the current token is an identifier, this method resolves it into a variable, an array entry, or a subroutine call.
        '''
        
        '''
        Implementation logic: integerConstant|stringConstant|keywordConstant|varName|
                              varName'['expression']' | subroutineCall | '('expression')' | unaryOp term
        subroutineCall: subroutineName '(' expressionList ')' 
                        | (className|varName) '.' subroutineName '(' expressionList ')'
        '''
        subroot = ET.SubElement(root, 'term')

        # term =  '('expression')' 
        if self.tokenizer.symbol() == '(':
            node = ET.SubElement(subroot, 'symbol')
            node.text = self.tokenizer.symbol()

            self.tokenizer.advance()
            self.compile_expression(subroot)

            assert self.tokenizer.symbol() == ')'
            node = ET.SubElement(subroot, 'symbol')
            node.text = self.tokenizer.symbol()
            self.tokenizer.advance()
        # term = unaryOp term
        elif self.tokenizer.symbol() in JackLexicon.unaryOp:
            node = ET.SubElement(subroot, 'symbol')
            node.text = self.tokenizer.symbol()

            self.tokenizer.advance()
            self.compile_term(subroot)
        # term = integerConstant
        elif self.tokenizer.token_type() == JackLexicon.INT_CONST:
            node = ET.SubElement(subroot, 'integerConstant')
            node.text = self.tokenizer.int_value()
            self.tokenizer.advance()
        # term = stringConstant
        elif self.tokenizer.token_type() == JackLexicon.STRING_CONST:
            node = ET.SubElement(subroot, 'stringConstant')
            node.text = self.tokenizer.string_value()
            self.tokenizer.advance()
        # term = keywordConstant
        elif self.tokenizer.token_type() == JackLexicon.KEYWORD:
            node = ET.SubElement(subroot, 'keyword')
            node.text = self.tokenizer.keyword()
            self.tokenizer.advance()
        # term = varName | varName'['expression']' | subroutineName '(' expressionList ')' 
        #                | (className|varName) '.' subroutineName '(' expressionList ')'
        else:
            assert self.tokenizer.token_type() == JackLexicon.IDENTIFIER
            node = ET.SubElement(subroot, 'identifier')
            node.text = self.tokenizer.identifier()
            
            next = self.tokenizer.advance()

            # term = varName'['expression']'
            if next == '[':
                node = ET.SubElement(subroot, 'symbol')
                node.text = self.tokenizer.symbol()

                self.tokenizer.advance()
                self.compile_expression(subroot)

                assert self.tokenizer.symbol() == ']'
                node = ET.SubElement(subroot, 'symbol')
                node.text = self.tokenizer.symbol()
                self.tokenizer.advance()
            # term = subroutineName '(' expressionList ')' 
            elif next == '(':
                node = ET.SubElement(subroot, 'symbol')
                node.text = self.tokenizer.symbol()

                self.tokenizer.advance()
                self.compile_expression_list(subroot)

                assert self.tokenizer.symbol() == ')'
                node = ET.SubElement(subroot, 'symbol')
                node.text = self.tokenizer.symbol()
                self.tokenizer.advance()
            # term = (className|varName) '.' subroutineName '(' expressionList ')'
            elif next == '.':
                node = ET.SubElement(subroot, 'symbol')
                node.text = self.tokenizer.symbol()

                name = self.tokenizer.advance()
                node = ET.SubElement(subroot, 'identifier')
                node.text = name

                assert self.tokenizer.advance() == '('
                node = ET.SubElement(subroot, 'symbol')
                node.text = self.tokenizer.symbol()

                self.tokenizer.advance()
                self.compile_expression_list(subroot)

                assert self.tokenizer.symbol() == ')'
                node = ET.SubElement(subroot, 'symbol')
                node.text = self.tokenizer.symbol()
                self.tokenizer.advance()
            # term = varName
            else:
                return

    def compile_expression_list(self, root):
        '''
        Compile a (possibly empty) comma-seperated list of expressions.
        Return the number of expressions in the list.
        '''
        # Implementation logic: (expression (',' expression)* )?
        subroot = ET.SubElement(root, 'expressionList')
        subroot.text = '\n\t\t'    # prevent the node from being a null node

        if self.tokenizer.symbol() != ')':
            # Add expression
            self.compile_expression(subroot)

            while self.tokenizer.symbol() != ')':    # as expressionList only exists like '(' expressionList ')'
                # Add symbol ','
                assert self.tokenizer.symbol() == ','
                node = ET.SubElement(subroot, 'symbol')
                node.text = self.tokenizer.symbol()
                # Add expression
                self.tokenizer.advance()
                self.compile_expression(subroot)