import JackLexicon
import xml.etree.ElementTree as ET


class JackTokenizer:
    """
    Ignore all comments and white space, get the next token, and advance the input just beyond it.
    """

    def __init__(self, input_file):
        """
        Open the input .jack file and get ready to tokenize it.
        """
        self.commands = ''    # a complete string composed of all commands withoud comments
        with open(input_file, 'r') as file:
            for line in file.readlines():
                line = line.strip('\n').strip()
                if line[0:2]=='//' or line[0:2]=='/*' or line[0:1]=='*':     # a simplification, fail for situations like '/* xxx */ var int x; '
                    continue
                else:
                    self.commands += line.split('//')[0].split('/*')[0].strip()    # remove comments if there are

        self.curr_token = ''
        self.curr_index = -1

    def has_more_tokens(self):
        """
        Return if there are more tokens in the input.
        """
        return self.curr_index + 1 < len(self.commands)

    def advance(self):
        '''
        Get the next token from the input, and make it the current token.
        This method should be called only if has_more_tokens() returns True.
        Initially there is no current token.
        '''
        while self.commands[self.curr_index + 1] == ' ':
            self.curr_index += 1
        st = self.curr_index + 1

        # The current token is a integar constant.
        if self.commands[st].isdigit():
            end = st + 1
            while end < len(self.commands) and self.commands[end].isdigit():
                end += 1
            self.curr_token = self.commands[st:end]
            self.curr_index = end - 1

        # The current token is a string consant.
        elif self.commands[st] == '"':
            end = st + 1
            while end < len(self.commands) and self.commands[end] != '"':
                end += 1
            self.curr_token = self.commands[st:end+1]
            self.curr_index = end

        # The current token is an identifier (a sequence of letters, digits, and underscore '_' not starting with a digit).
        elif self.commands[st].isalpha() or self.commands[st] == '_':
            end = st + 1
            while end < len(self.commands) and (self.commands[end].isalpha()
                                                or self.commands[end].isdigit()
                                                or self.commands[end] == '_'):
                end += 1
            self.curr_token = self.commands[st:end]
            self.curr_index = end - 1
            
        # The current token is a symbol composed of one character.
        elif self.commands[st] in JackLexicon.symbol:
            self.curr_token = self.commands[st]
            self.curr_index += 1

        return self.curr_token
    
    def token_type(self):
        '''
        Return the type of the current token, as a constant.
        '''
        if self.curr_token in JackLexicon.symbol:
            return JackLexicon.TokenType.SYMBOL
        elif self.curr_token in JackLexicon.keyword:
            return JackLexicon.TokenType.KEYWORD
        elif self.curr_token.isdigit():
            return JackLexicon.TokenType.INT_CONST
        elif self.curr_token[0] == '"':
            return JackLexicon.TokenType.STRING_CONST
        else:
            return JackLexicon.TokenType.IDENTIFIER

    def keyword(self):
        '''
        Return the keyword which is the current token.
        This method should be called only of token_type() returns KEYWORD.
        '''
        return self.curr_token

    def symbol(self):
        '''
        Return the character which is the current token.
        This method should be called only if token_type() returns SYMBOL.
        '''
        return self.curr_token

    def identifier(self):
        '''
        Return the string which is the current token.
        This method should be called only if token_type() returns IDENTIFIER.
        '''
        return self.curr_token

    def int_value(self):
        '''
        Return the integer value of the current value.
        This method should be called only if token_type() returns INT_CONST.
        '''
        return self.curr_token

    def string_value(self):
        '''
        Return the string value of the current value, without the opening and closing double quotes.
        This method should be called only if token_type() returns STRING_CONST.
        '''
        return self.curr_token[1:-1]

    def test(self, input_file):
        '''
        Output an .xml file which will be compared with the compare-file to ensure the correctness of the Tokenizer.
        '''
        root = ET.Element("tokens")
        while self.has_more_tokens():
            self.advance()
            ttype = self.token_type()
            if ttype == JackLexicon.KEYWORD:
                token = ET.SubElement(root, 'keyword')
                token.text = self.keyword()
            elif ttype == JackLexicon.SYMBOL:
                token = ET.SubElement(root, 'symbol')
                token.text = self.symbol()
            elif ttype == JackLexicon.IDENTIFIER:
                token = ET.SubElement(root, 'identifier')
                token.text = self.identifier()
            elif ttype == JackLexicon.INT_CONST:
                token = ET.SubElement(root, 'integerConstant')
                token.text = self.int_value()
            elif ttype == JackLexicon.STRING_CONST:
                token = ET.SubElement(root, 'stringConstant')
                token.text = self.string_value()

        tree = ET.ElementTree(root)
        ET.indent(tree)
        output_file = input_file.replace('.jack', 'T.xml')
        tree.write(output_file)
