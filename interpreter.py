class NobleInterpreter:

    def __init__(self, tree, env):
        self.env = env
        self.commands = ['leave']
        
        result = self.walkTree(tree)
        if result is not None and (isinstance(result, int) or isinstance(result, str) or isinstance(result, float)):
           print(result)

    def walkTree(self, node):
    
        if isinstance(node, int) or isinstance(node, str) or isinstance(node, float):
           return node
           
        if node is None:
           return None
           
        if node[0] == 'program':
           if node[1] != None:
              self.walkTree(node[1])
           self.walkTree(node[2])
           
        if node[0] == 'command':
           cmd = node[1]
           if cmd == 'leave':
              exit(0)

        if node[0] == 'num' or node[0] == 'str' or node[0] == 'float':
           return node[1]

        if node[0] == 'add':
           try:
              return self.walkTree(node[1]) + self.walkTree(node[2])
           except:
              pass
              
        elif node[0] == 'sub':
           try:
              return self.walkTree(node[1]) - self.walkTree(node[2])
           except:
              pass
              
        elif node[0] == 'mul':
           try:
              return self.walkTree(node[1]) * self.walkTree(node[2])
           except:
              pass
              
        elif node[0] == 'exp':
           try:
              return self.walkTree(node[1]) ** self.walkTree(node[2])
           except:
              pass
              
        elif node[0] == 'root':
           try:
              num = 1/self.walkTree(node[2])
              return self.walkTree(node[1]) ** num
           except:
              pass
              
        elif node[0] == 'div':
           try:
              return self.walkTree(node[1]) / self.walkTree(node[2])
           except:
              pass
              
        elif node[0] == 'int_div':
           try:
              return self.walkTree(node[1]) // self.walkTree(node[2])
           except:
              pass
           
        elif node[0] == 'mod':
           try:
              return self.walkTree(node[1]) % self.walkTree(node[2])
           except:
              pass
        
        if node[0] == 'add_assign':
           try:
              note = node[1]
              var = self.env[node[1]]
              val = var + self.walkTree(node[2])
              self.env[node[1]] = val
           except LookupError:
              print("Undefined variable '"+note+"' found!")
        
        if node[0] == 'add_assign_var':
           try:
              note = node[1]
              var = self.env[node[1]]
              note = node[2]
              val = var + self.env[node[2]]
              self.env[node[1]] = val
           except LookupError:
              print("Undefined variable '"+note+"' found!")
              
        if node[0] == 'sub_assign':
           try:
              note = node[1]
              var = self.env[node[1]]
              val = var - self.walkTree(node[2])
              self.env[node[1]] = val
           except LookupError:
              print("Undefined variable '"+note+"' found!")
        
        if node[0] == 'sub_assign_var':
           try:
              note = node[1]
              var = self.env[node[1]]
              note = node[2]
              val = var - self.env[node[2]]
              self.env[node[1]] = val
           except LookupError:
              print("Undefined variable '"+note+"' found!")
              
        if node[0] == 'mul_assign':
           try:
              note = node[1]
              var = self.env[node[1]]
              val = var * self.walkTree(node[2])
              self.env[node[1]] = val
           except LookupError:
              print("Undefined variable '"+note+"' found!")
        
        if node[0] == 'mul_assign_var':
           try:
              note = node[1]
              var = self.env[node[1]]
              note = node[2]
              val = var * self.env[node[2]]
              self.env[node[1]] = val
           except LookupError:
              print("Undefined variable '"+note+"' found!")
              
        if node[0] == 'div_assign':
           try:
              note = node[1]
              var = self.env[node[1]]
              val = var / self.walkTree(node[2])
              self.env[node[1]] = val
           except LookupError:
              print("Undefined variable '"+note+"' found!")
        
        if node[0] == 'div_assign_var':
           try:
              note = node[1]
              var = self.env[node[1]]
              note = node[2]
              val = var / self.env[node[2]]
              self.env[node[1]] = val
           except LookupError:
              print("Undefined variable '"+note+"' found!")
             
           
        if node[0] == 'var_assign':
           self.env[node[1]] = self.walkTree(node[2])
        
        if node[0] == 'var':
           try:
              if node[1] not in self.commands:
                 return self.env[node[1]]
              else:
                 return node[1]
           except LookupError:
              print("Undefined variable '"+node[1]+"' found!")