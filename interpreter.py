class NobleInterpreter:

    def __init__(self, tree, env):
        self.env = env
        
        result = self.walkTree(tree)
        if result is not None and (isinstance(result, int) or isinstance(result, str)):
           print(result)

    def walkTree(self, node):
    
        if isinstance(node, int) or isinstance(node, str):
           return node
           
        if node is None:
           return None
           
        if node[0] == 'program':
           if node[1] != None:
              self.walkTree(node[1])
           self.walkTree(node[2])

        if node[0] == 'num' or node[0] == 'str':
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
              
        elif node[0] == 'div':
           try:
              return self.walkTree(node[1]) / self.walkTree(node[2])
           except:
              pass
           
        elif node[0] == 'mod':
           try:
              return self.walkTree(node[1]) % self.walkTree(node[2])
           except:
              pass
           
        if node[0] == 'var_assign':
           self.env[node[1]] = self.walkTree(node[2])
        
        if node[0] == 'var':
           try:
              if node[1] != 'leave':
                 return self.env[node[1]]
              else:
                 exit(0)
           except LookupError:
              print("Undefined variable '"+node[1]+"' found!")
              
              