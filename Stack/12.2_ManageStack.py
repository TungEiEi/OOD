class Stack :
    def __init__(self , list = None):
        if list == None :
            self.items = []
        else :
            self.items = list

    def __str__(self) -> str:
        ans = []
        for element in self.items :
            ans.append(int(element))
        return f"Value in Stack = {ans}"
    
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
    
def ManageStack(list):
    s = Stack()
    for str in list:
        if str[:1] == 'A':
            s.push(str[2:])
            print(f"Add = {str[2:]}")
            # print(f"Value in Stack = {s.items}")
        elif str[:1] == 'P':
            if s.isEmpty():
                print(-1)
            else:
                print(f"Pop = {s.pop()}")
                # print(f"Value in Stack = {s.items}")
        elif str[:1] == 'D':
            if s.isEmpty():
                print(-1)
            else:
                temp = Stack()
                for ele in reversed(s.items):
                    if ele != str[2:]:
                        temp.push(s.pop())
                    else:
                        s.pop()
                        print(f"Delete = {str[2:]}")
                while not temp.isEmpty():
                    s.push(temp.pop())
                    
        elif str[:2] == 'LD':
            if s.isEmpty():
                print(-1)
            else:
                temp = Stack()
                for ele in reversed(s.items):
                    if int(ele) >= int(str[2:]):
                        temp.push(s.pop())
                    else:
                        s.pop()
                        print(f"Delete = {ele} Because {ele} is less than{str[2:]}")
                while not temp.isEmpty():
                    s.push(temp.pop())
        elif str[:2] == 'MD':
            if s.size == 0 or s.isEmpty():
                print(-1)
            else:
                temp = Stack()
                for ele in reversed(s.items):
                    if int(ele) <= int(str[2:]):
                        temp.push(s.pop())
                    else:
                        s.pop()
                        print(f"Delete = {ele} Because {ele} is more than{str[2:]}")
                while not temp.isEmpty():
                    s.push(temp.pop())
    print(s)

ManageStack(input("Enter Input : ").split(","))

