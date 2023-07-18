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

    def deleteStack(self,x):
        temp = Stack()
        for i in reversed(self.items):
            if i == x:
                self.pop()
            else:
                temp.push(self.pop())
        while not temp.isEmpty():
                self.push(temp.pop())

def parkinglot(list):
    s = Stack()
    for car in list[1]:
        if car != '0' and car != ',':
            s.push(int(car))

    if list[2] == 'arrive':
        if s.size() < int(list[0]):
            if int(list[3]) in s.items:
                print(f"car {list[3]} already in soi")
            else:
                s.push(int(list[3]))
                print(f"car {s.peek()} arrive! : Add Car {s.peek()}")
        else:
            print(f"car {list[3]} cannot arrive : Soi Full")

    elif list[2] == 'depart':
        if int(list[3]) in s.items:
            s.deleteStack(int(list[3]))
            print(f"car {list[3]} depart ! : Car {list[3]} was remove")
        elif list[1] == '0':
            print(f"car {list[3]} cannot depart : Soi Empty")
        else:
            print(f"car {list[3]} cannot depart : Dont Have Car {list[3]}")

    return s.items

print("******** Parking Lot ********")

Input = input("Enter max of car,car in soi,operation : ").split()

print(parkinglot(Input))
