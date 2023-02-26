import random
def swapItems(items, index1, index2):
        temp = items[index1]
        items[index1] = items[index2]
        items[index2] = temp
        return items

def randomiseArray(array):
    for i in range(1000):
        swapItems(array, random.randint(0,len(array)-1), random.randint(0,len(array)-1))

    return array

def newRandomArray(length):
    array = []
    for i in range(length):
        array.append(i+1)
    return randomiseArray(array)

def mergeSortStart(array):
    return mergeSort(array, 0, len(array)-1)

def mergeSort(array, left, right):
    if left<right:
        center = (right + left) // 2
        array = mergeSort(array, left, center)
        array = mergeSort(array, center+1, right)
        array = merge(array, left,center, right)
        
    return array

def merge(array, left, center, right):
    lp = left
    b = ["" for i in range(right-left+1)]
    bp = 0
    rp = center + 1
    
    while lp <= center and rp <= right:
        
        if array[lp] <= array[rp]:
            b[bp] = array[lp]
            bp+=1
            lp+=1
        else:
            b[bp] = array[rp]
            bp+=1
            rp+=1
    if lp>center:
        while rp <= right:
            b[bp] = array[rp]
            bp+=1
            rp+=1
    else:
        
        while lp<=center:
            b[bp] = array[lp]
            bp+=1
            lp+=1
    for i in range(right-left+1):
        array[left+i] = b[i]
    return array


print(mergeSortStart(newRandomArray(20)))
        
