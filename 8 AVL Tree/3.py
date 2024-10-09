def fineN(n):
    if tree[n] != -1:
        return tree[n]
    
    fineN(2*n+1)
    fineN(2*n+2)
    tree[n] = min(tree[2*n+1], tree[2*n+2])
    tree[2*n+1] -= tree[n]
    tree[2*n+2] -= tree[n]

node, data = input('Enter Input : ').split('/')
node, data = int(node), list(map(int, data.split()))
if len(data) == node//2+1:
    tree = [-1] * node
    for x in range(len(data)):
        tree[node//2+x] = data[x]
    fineN(0)
    print(sum(tree))
else:
    print('Incorrect Input')