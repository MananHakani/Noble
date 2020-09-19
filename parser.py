from sly import Parser
from lexer import NobleLexer

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
        
    @_('NAME ASSIGN1 expr')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.expr)
        
    @_('NAME ASSIGN1 DQOUTE')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.DQOUTE)
        
    @_('NAME ASSIGN1 SQOUTE')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.SQOUTE)
        
    @_('NAME ASSIGN2 expr')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.expr)
        
    @_('NAME ASSIGN2 DQOUTE')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.DQOUTE)
        
    @_('NAME ASSIGN2 SQOUTE')
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
     
    @_('expr DIV expr')
    def expr(self, p):
        return ('div', p.expr0, p.expr1)
        
    @_('expr MODULAS expr')
    def expr(self, p):
        return ('mod', p.expr0, p.expr1)
        
    @_('SUB expr %prec UMINUS')
    def expr(self, p):
        return p.expr
        
    @_('NAME')
    def expr(self, p):
        return ('var', p.NAME)
        
    @_('NUMBER')
    def expr(self, p):
        return ('num', p.NUMBER)
        
    @_('DQOUTE')
    def expr(self, p):
        return ('str', p.DQOUTE)
        
    @_('SQOUTE')
    def expr(self, p):
        return ('str', p.SQOUTE)
        
    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr