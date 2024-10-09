def insertionSort(sequence, index=1):
    if index == len(sequence):
        return print('sorted')

    insertLeft(sequence, index)

    if len(sequence[0:index+1]) != 0:
        print(sequence[0:index+1], end=' ')
    if len(sequence[index+1:]) != 0:
        print(sequence[index+1:], end=' ')
    print()

    insertionSort(sequence, index+1)

def insertLeft(sequence, index):
    if index-1 < 0:
        return print(f"insert {sequence[index]} at index {index} : ", end='')

    if sequence[index-1] > sequence[index]:
        sequence[index], sequence[index-1] = sequence[index-1], sequence[index]
        insertLeft(sequence, index-1)
    else:
        print(f"insert {sequence[index]} at index {index} : ", end='')

inp = list(map(int,input("Enter Input : ").split()))
insertionSort(inp)
print(inp)