def sort_without_negative(a):
    # Store all non-negative values
    ans=[]
    for i in range(len(a)):
        if (a[i] >= 0):
            ans.append(a[i])
    # Sort non-negative values
    ans = sortArray(ans)

    j = 0
    for i in range(len(a)):
        if (a[i] >= 0):
            a[i] = ans[j]
            j += 1

    for i in range(len(a)):
        print(a[i],end = " ")

def sortArray(list):
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            if list[i] >= list[j]:
                list[i], list[j] = list[j],list[i]
    return list

inp = [int(x) for x in input("Enter Input : ").split()]
sort_without_negative(inp)
