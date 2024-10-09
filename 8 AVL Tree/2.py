class BST:
    class Node:
        def __init__(self, data, left = None, right = None):
            self.data = data
            self.left = None if left is None else left
            self.right = None if right is None else right
        
        def __str__(self):
            s = str(self.data)
            return s
    
    def __init__(self, root = None):
        self.root = None if root is None else root
        
    def add(self, data):
        self.root = BST._add(self.root, data)
        

    def _add(root, data):
        if root is None:
            return BST.Node(data)
        else:
            if data < root.data:
                root.left = BST._add(root.left, data)
            else:
                root.right = BST._add(root.right, data)
        return root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

def closestValue(root, value, close = None):
    if root is None:
        return close
    if close is None:
        close = root.data
    else:
        dc = abs(value - close)
        dr = abs(root.data - value)
        if dr < dc:
            close = root.data
        elif dr == dc:
            close = max(root.data,close)     
    L = closestValue(root.left, value, close)
    R = closestValue(root.right, value, close)
    s,m,b = sorted(sorted([close,L,R], reverse=True),key=lambda a: abs(a-value)) #sorted base--> น้อย ---> ไป
    return s
    # 8 4 2/3
    # 5 1 1
    # 1 1 5(sorted)(คือ ความสำคัญ ไม่ใช่ value)
#print    4 2 8
        

tree = BST()
data = input("Enter Input : ").split("/")
for e in data[0].split():
    tree.add(int(e))
    tree.printTree(tree.root)
    print("--------------------------------------------------")
print(f"Closest value of {data[1]} : {closestValue(tree.root,int(data[1]))}")
