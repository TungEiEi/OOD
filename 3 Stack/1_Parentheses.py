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

def match2(op,cl):
    opens = "([{"
    closes = ")]}"
    return opens.index(op) == closes.index(cl)  

def parenMatching(str):
    s = Stack()
    i= 0  # index : str[i]
    error = 0
    while i< len(str) and error == 0 :
        c = str[i]
        if c in'{[(':
            s.push(c)
        else:
            if c in'}])':
                if s.size() > 0:
                    if not match2(s.pop(),c):
                        error = 1 # open & close not match
                else: # empty stack 
                        error = 2 # no open paren
        i+= 1
    if s.size() > 0:  # stack not empty
        error = 3 # open paren(s) excesses
    
    return error,c,i,s

str = input("Enter Input : ")
err,c,i,s= parenMatching(str)
# if err == 1:
#     print(str, 'unmatchopen-close  ')
# elif err == 2:
#     print(str, 'close parenexcess')
# elif err == 3:
#     print(str, 'open paren(s) excess  ', s.size(),': ',end=''  ) 
#     for ele in s.items:
#         print(ele,sep=' ',end = '')
#         print()
# else: 
#     print(str, 'MATCH')
if err == 0:
    print("Parentheses : Matched ! ! !")
else:
    print("Parentheses : Unmatched ! ! !")