def quick_sort(l):
    if len(l) <= 1:
        return l
    else:
        return quick_sort([e for e in l[1:] if e > l[0]]) + [l[0]] +\
            quick_sort([e for e in l[1:] if e <= l[0]])
        
inp = [int(x) for x in input("Enter your List : ").split(",")]
print("List after Sorted :", quick_sort(inp))