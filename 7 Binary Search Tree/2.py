class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = BST.add(self.root, data)

    def add(root, data):
        if root is None:
            return Node(data)
        else:
            if data < root.data:
                root.left = BST.add(root.left, data)
            else:
                root.right = BST.add(root.right, data)
            return root
        
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

def find_min(root):
    global min
    if root.left is None:
        min = root.data
        return min
    else:
        find_min(root.left)
        return min

def find_max(root):
    global max
    if root.right is None:
        max = root.data
        return max
    else:
        find_max(root.right)
        return max

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    T.insert(i)
T.printTree(T.root)
print("--------------------------------------------------")
print("Min :",find_min(T.root))
print("Max :",find_max(T.root))