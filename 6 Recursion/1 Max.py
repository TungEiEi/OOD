def Max(list):
    if len(list) == 1:
        return list[0]
    else:
        m = Max(list[1:])
        return m if m > list[0] else list[0]

inp = [int(x) for x in input("Enter Input : ").split()]
print("Max :", Max(inp))
