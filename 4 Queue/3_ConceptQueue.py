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
    
inp = input("input : ").split(",")
count = 0
num_deq = 0
num_inp = 0
q = Queue()
for str in inp:
    print("Step :",str)
    if str[0] == 'E':
        for i in range(int(str[1:])):
            q.add(f'*{count}')
            count +=1
        print("Enqueue :",q.items)
    elif str[0] == 'D':
        for i in range(int(str[1])):
            if not q.isEmpty():
                q.remove()
            else:
                num_deq+=1
        print("Dequeue :",q.items)
    else:
        print(q.items)
        num_inp+=1
    print("Error Dequeue :",num_deq)
    print("Error input :",num_inp)
    print("--------------------")