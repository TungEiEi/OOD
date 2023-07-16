class Stack :
    def __init__(self , list = None):
        if list == None :
            self.items = []
        else :
            self.items = list

    def __str__(self) -> str:
        s = f"stack of {str(self.size())} items :"
        for element in self.items :
            s += f"{str(element)} "
        return s
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        try :
           return self.items[-1]
        except :
            return 0
        
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
def infix2postfix(infix):
    postfix = []
    s = Stack()
    operators = ['(',')','+','-','*','/','^']
    prioritys = [0,0,3,3,5,5,7]

    def priority(x):
        return prioritys[operators.index(x)]

    for str in infix:
        if str not in operators:
            postfix.append(str)
        else:
            if s.isEmpty() or priority(s.items[-1]) < priority(str):
                s.push(str)
            elif str == '(':
                s.push(str)
            elif priority(s.items[-1]) == priority(str):
                postfix.append(s.pop())
                s.push(str)
            elif priority(s.items[-1]) > priority(str):
                while not s.isEmpty() and s.items[-1] != "(":
                    postfix.append(s.pop())
                s.push(str)
                if str == ')':
                    [s.pop() for i in range(2)]
        # print(s.items)

    while not s.isEmpty():
        postfix.append(s.pop())

    return  ''.join(postfix)

print(" ***Infix to Postfix***")

token = input("Enter Infix expression : ")

print("PostFix : ")

print(infix2postfix(token))
