def bubble(l):
    for last in range(len(l)-1, 0, -1):
        swaped = False
        for i in range(last):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                swaped = True
        if not swaped:
            break

l1 = [5,6,2,3,0,1,4]
bubble(l1)

def selection(l):
    for last in range(len(l)-1, 0, -1):
        biggest = l[0]
        biggest_i = 0
        for i in range(1, last+1):
            if l[i] > biggest:
                biggest = l[i]
                biggest_i = i
        l[last], l[biggest_i] = l[biggest_i], l[last]

l2 = [5,6,2,3,0,1,4]
selection(l2)

def insertion(l):
    for i in range(1, len(l)):
        iEle = l[i]
        for j in range(i, -1, -1):
            if iEle < l[j-1] and j > 0:
                l[j] = l[j-1]
            else:
                l[j] = iEle
                break

l3 = [5,6,2,3,0,1,4]
insertion(l3)

def shell(l, dIncrements):
    for inc in dIncrements:
        for i in range(inc, len(l)):
            iEle = l[i]
            for j in range(i, -1, -inc):
                if iEle<l[j-inc] and j>=inc:
                    l[j] = l[j-inc]
                else:
                    l[j] = iEle
                    break

l4 = [10,11,1,13,2,6,4,12,5,8,7,9,3]
dIncrements = [5,3,1]
shell(l4, dIncrements)

from math import log2
from math import floor

def print90(h, i, max_i):
    if i < max_i:
        indent = floor(log2(i+1))
        print90(h, (i*2)+2, max_i)
        print('  '*indent, h[i])
        print90(h, (i*2)+1, max_i)
def insertMinHeap(h, i):
    print('insert', h[i], 'at index', i, end='    ')
    print(h)
    insertEle = h[i]
    fi = (i-1)//2
    while i>0 and insertEle < h[fi]:
        h[i] = h[fi]
        i = fi
        fi = (i-1)//2
    h[i] = insertEle

# h1 = [30, 85, 97, 100, 200]
# for i in range(1, len(h1)):
#     insertMinHeap(h1, i)
#     print(h1)
#     print90(h1, 0, i)
#     print('---------------\n')

def delMin(h, last):
    print('delMin', h[0], 'last index = ', last, end='    ')
    print(h)
    insertEle = h[last]
    h[last] = h[0]
    hole = 0
    ls = hole*2+1
    found = False
    while ls > last and not found:
        rs = ls if ls+1 >= last else ls+1
        min = ls if h[ls] < h[rs] else rs
        if h[min] < insertEle:
            h[hole] = h[min]
            hole = min
            ls = hole*2+1
        else:
            found = True
    h[hole] = insertEle

# h2 = [13,14,16,24,21,19,68,65,26,32,31]
# for last in range(len(h2)-1, -1, -1):
#     delMin(h2, last)
#     print(h2)
#     print90(h2, 0, last)
#     print('----------------\n')

def merge(l, left, right, rightEnd):
    start = left
    leftEnd = right-1
    result = []
    while left<=leftEnd and right<=rightEnd:
        if l[left] < l[right]:
            result.append(l[left])
            left+=1
        else:
            result.append(l[right])
            right+=1
    while left<=leftEnd:
        result.append(l[left])
        left+=1
    while right<=rightEnd:
        result.append(l[right])
        right+=1
    for ele in result:
        l[start] = ele
        start+=1
        if start > rightEnd:
            break
def mergeSort(l, left, right):
    center = (left+right)//2
    if left < right:
        mergeSort(l, left, center)
        mergeSort(l, center+1, right)
        merge(l, left, center+1, right)

l5 = [5,3,6,1,2,7,8,4]
mergeSort(l5, 0, len(l5)-1)

def quick(l, left, right):
    if left == right+1:
        if l[left] > l[right]:
            l[left], l[right] = l[right], l[left]
        return
    if left<right:
        pivot = l[left]
        i, j = left+1, right
        while i<j:
            while i<right and l[i]<=pivot:
                i+=1
            while j>left and l[j]>=pivot:
                j-=1
            if i<j:
                l[i], l[j] = l[j], l[i]
        if left is not j:
            l[left], l[j] = l[j], pivot
        quick(l, left, j-1)
        quick(l, j+1, right)

l6 = [5,1,4,9,6,3,8,2,7,0]
quick(l6, 0, len(l6)-1)
print(l6)