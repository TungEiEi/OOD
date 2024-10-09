class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'{self.data}'


class LinkedList:
    def __init__(self, node = None):
        self.size = 0
        self.head = node
        self.tail = None
        if node:
            self.size += 1
            self.tail = node

    def add_right(self, data):
        self.size += 1
        node = Node(data)
        # if there is only one element in linkedlist tail will point to head
        if not self.head:
            self.head = node
            self.tail = node
            self.head.next = self.tail
        else:
            self.tail.next = node
            self.tail = node

    def add_left(self, data):
        self.size += 1
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = self.head
            self.head.next = self.tail
        elif self.size == 2:
            self.tail = self.head
            self.tail.next = None
            node.next = self.head
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def is_empty(self):
        return self.size == 0

    def insert(self, pos, data):
        if pos < 0 or pos > self.size:
            return 0
        if pos == 0:
            self.add_left(data)
            return 1
        if pos == self.size:
            self.add_right(data)
            return 1
        self.size += 1
        node = Node(data)
        index = 0
        current_node = self.head
        prev_node = None
        while current_node:
            if index == pos:
                break
            index += 1
            prev_node = current_node
            current_node = current_node.next
        prev_node.next = node
        node.next = current_node
        return 1

    def __repr__(self):
        return f"{self.get_item()}"

    def get_item(self):
        res = []
        current_node = self.head
        if self.head == self.tail:
            return [self.head]
        while current_node:
            res.append(current_node)
            current_node = current_node.next
        return res
    
inp = input("Enter Input : ").split(",")
l1 = LinkedList()
[l1.add_right(item) for item in inp[0].split()]
if l1.is_empty():
    print("List is empty")
else:
    items = l1.get_item()
    print('link list : ' + '->'.join([str(node.data) for node in items]))
for i in inp[1:]:
    node,data = map(int,i.split(":"))
    if node >= 0 and node <= l1.size:
        l1.insert(node, data)
        print(f"index = {node} and data = {data}")
    else:
        print("Data cannot be added")
        
    if l1.is_empty():
        print("List is empty")
    else:
        items = l1.get_item()
        print('link list : ' + '->'.join([str(node.data) for node in items]))
