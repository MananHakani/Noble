from sly import Lexer

class NobleLexer(Lexer):
    tokens = { NAME, NUMBER, DQOUTE, SQOUTE, LPAREN, RPAREN, ADD, SUB, MUL, DIV, ASSIGN1, ASSIGN2, MODULAS }
    ignore = '\t '
    literals = {'~', '=', '+', '-', '/', '*', '(', ')', ',', ';'}

    NAME = r'[a-zA-Z_][a-zA-Z_0-9]*'
    DQOUTE = r'\".*?\"'
    SQOUTE = r"\'.*?\'"
    LPAREN = r'\('
    RPAREN = r'\)'
    ADD = r'\+'
    SUB = r'-'
    MUL = r'\*'
    DIV = r'/'
    ASSIGN1 = '~'
    ASSIGN2 = '='
    MODULAS = r'%'

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'/#.*')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def newline(self, t):
        self.lineno = t.value.count('\n')