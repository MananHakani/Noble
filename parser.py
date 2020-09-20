from sly import Parser
from lexer import NobleLexer

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


class NobleParser(Parser):
    tokens = NobleLexer.tokens
    
    precedence = (
        ('left','ADD','SUB'),
        ('left','MUL','DIV'),
        ('right','UMINUS'),
    )

    def __init__(self):
        self.env = {}

    @_('')
    def statement(self, p):
        pass
        
    @_('var_assign')
    def statement(self, p):
        return p.var_assign
        
    @_('NAME ASSIGN expr')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.expr)
        
    @_('NAME ASSIGN DQOUTE')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.DQOUTE)
        
    @_('NAME ASSIGN SQOUTE')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.SQOUTE)
        
    @_('expr')
    def statement(self, p):
        return (p.expr)
        
    @_('expr ADD expr')
    def expr(self, p):
        return ('add', p.expr0, p.expr1)

    @_('expr SUB expr')
    def expr(self, p):
        return ('sub', p.expr0, p.expr1)
        
    @_('expr MUL expr')
    def expr(self, p):
        return ('mul', p.expr0, p.expr1)
        
    @_('expr MUL MUL expr')
    def expr(self, p):
        return ('exp', p.expr0, p.expr1)
        
    @_('expr MUL MUL MUL expr')
    def expr(self, p):
        return ('root', p.expr0, p.expr1)
     
    @_('expr DIV expr')
    def expr(self, p):
        return ('div', p.expr0, p.expr1)
        
    @_('expr DIV DIV expr')
    def expr(self, p):
        return ('int_div', p.expr0, p.expr1)
        
    @_('expr MODULAS expr')
    def expr(self, p):
        return ('mod', p.expr0, p.expr1)
        
    @_('SUB expr %prec UMINUS')
    def expr(self, p):
        return p.expr
        
    @_('NAME ADD ASSIGN expr')
    def expr(self, p):
        return ('add_assign', p.NAME, p.expr)
        
    @_('NAME ADD ASSIGN NAME')
    def expr(self, p):
        return ('add_assign_var', p.NAME0, p.NAME1)
        
    @_('NAME SUB ASSIGN expr')
    def expr(self, p):
        return ('sub_assign', p.NAME, p.expr)
        
    @_('NAME SUB ASSIGN NAME')
    def expr(self, p):
        return ('sub_assign_var', p.NAME0, p.NAME1)
        
    @_('NAME DIV ASSIGN expr')
    def expr(self, p):
        return ('div_assign', p.NAME, p.expr)
        
    @_('NAME DIV ASSIGN NAME')
    def expr(self, p):
        return ('div_assign_var', p.NAME0, p.NAME1)
        
    @_('NAME MUL ASSIGN expr')
    def expr(self, p):
        return ('mul_assign', p.NAME, p.expr)
        
    @_('NAME MUL ASSIGN NAME')
    def expr(self, p):
        return ('mul_assign_var', p.NAME0, p.NAME1)
        
    @_('NAME')
    def statement(self, p):
        return ('var', p.NAME)
        
    @_('NUMBER')
    def expr(self, p):
        return ('num', p.NUMBER)
        
    @_('FLOAT')
    def expr(self, p):
        return ('float', p.FLOAT)
        
    @_('DQOUTE')
    def expr(self, p):
        return ('str', p.DQOUTE)
        
    @_('SQOUTE')
    def expr(self, p):
        return ('str', p.SQOUTE)
        
    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr
           
    @_('DOLLAR NAME')
    def statement(self, p):
        return ('command', p.NAME)
        
        