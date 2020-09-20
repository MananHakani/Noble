from sly import Lexer

class NobleLexer(Lexer):
    tokens = { NAME, NUMBER, FLOAT, DQOUTE, SQOUTE, ADD, SUB, MUL, DIV, ASSIGN, MODULAS, LPAREN, RPAREN, DOLLAR }
    ignore = '\t '
    literals = {'=', '+', '-', '/', '*', '(', ')', ',', ';'}

    NAME = r'[a-zA-Z_][a-zA-Z_0-9]*'
    FLOAT = r'[0-9]+\.[0-9]+'
    DQOUTE = r'\".*?\"'
    SQOUTE = r"\'.*?\'"
    ADD = r'\+'
    SUB = r'-'
    MUL = r'\*'
    DIV = r'/'
    LPAREN = r'\('
    RPAREN = r'\)'
    ASSIGN = '='
    MODULAS = r'%'
    DOLLAR = r'\$'

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t
        
    @_(r'[0-9]+\.[0-9]+')
    def FLOAT(self, t):
        t.value = float(t.value)
        return t

    @_(r'/#.*')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def newline(self, t):
        self.lineno = t.value.count('\n')