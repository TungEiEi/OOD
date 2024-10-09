class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.snext = None
    
    def __repr__(self) -> str:
        return (str(self.data))
class Snode:
    def __init__(self,data):
        self.data = data
        self.snext = None
class link:
    def __init__(self):
        self.head = None
    def next_node(self,data:node):
        if self.search(data.data) is not None:
            return
        if self.head is None:
            self.head = data
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = data
        
        
            
    def search(self,data):
        cur = self.head

        while cur is not None:
            if cur.data == data:
                return cur
            cur = cur.next
        return None
        
        
    def next_secondary_node(self,n,data):
        cur = self.search(n)
        if cur is not None:
            while cur.snext is not None:
                cur = cur.snext
            cur.snext = data
        
    def show_all(self):
        cur = self.head
        while cur is not None:
            print(f"{cur} : ", end="")
            s_cur = cur.snext
            while s_cur is not None:
                print(s_cur.data, end=",")
                s_cur = s_cur.snext
            print()
            cur = cur.next
    



inp = input("input : ").split(",")
l = link()
for i in inp:
    u = i.split(" ")
    if u[0] == "ADN":
        l.next_node(node(u[1]))
    elif u[0] == "ADSN":
        h = u[1].split("-")
        l.next_secondary_node(h[0],Snode(h[1]))
l.show_all()