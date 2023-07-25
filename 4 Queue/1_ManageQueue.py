class Queue:

    def __init__(self , list = None):
        if list == None :
            self.items = []
        else :
            self.items = list

    def add(self,item):
        self.items.append(item)

    def remove(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
def ManageQueue(list):
    q = Queue()
    for str in list:
        if str[0] == "E":
            print(f"Add {str[2:]} index is {q.size()}")
            q.add(str[2:])
        else:
            if q.isEmpty():
                print(-1)
            else:
                print(f"Pop {q.remove()} size in queue is {q.size()}")
    if q.isEmpty():
        return "Empty"            

    return f"Number in Queue is :  {q.items}"

inp = input("Enter Input : ").split(",")

print(ManageQueue(inp))
