def bubble_sort(arr, i, count):
    if count == len(arr):
        return arr
    if i == len(arr)-1:
         i = 0
         return bubble_sort(arr, i, count + 1)
    if arr[i] > arr[i+1]:
        temp = arr[i]
        arr[i] = arr[i + 1]
        arr[i + 1] = temp
        return bubble_sort(arr, i + 1, count)
    bubble_sort(arr, i + 1, count)
    return arr

inp = [int(x) for x in input("Enter Input : ").split()]

print(bubble_sort(inp, 0, 0))