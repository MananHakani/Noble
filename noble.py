from lexer import NobleLexer
from parser import NobleParser
from interpreter import NobleInterpreter

if __name__ == "__main__":
   lexer = NobleLexer()
   parser = NobleParser()
   env = {}
   print('Noble Language\n© 2020 copyright: Ajay Lingayat\n')

   while True:
       try:
          txt = input('~~> ')
       except EOFError:
          break
          
       if txt:
          tree = parser.parse(lexer.tokenize(txt))
          NobleInterpreter(tree, env)