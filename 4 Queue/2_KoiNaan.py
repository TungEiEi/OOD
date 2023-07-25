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
    
    def peek(self):
        try :
           return self.items[0]
        except :
            return 0

inp = input("Enter people : ")

q = Queue()
q1 = Queue()
q2 = Queue()
i = 0
[q.add(str) for str in inp]

while not q.isEmpty():
    i+=1
    if i%3 == 1 and i > 1:
        q1.remove()
    if q1.size() < 5:
        q1.add(q.peek())
    elif q1.size() == 5:
        q2.add(q.peek())
    if i%2 == 0 and q2.size() > 1:
        q2.remove()
        
    q.remove()
    print(i,q.items,q1.items,q2.items)