from typing import List
# Move zero to the end of the array and keep the order of none zero elements.

def moveZeros(arr: List[int]):
    j = 0
    n = len(arr)
    for num in arr:
        if num != 0:
            arr[j] = num
            j += 1
    for i in range(j, n):
        arr[i] = 0
    return arr


def moveZeros2(arr):
    for i in range(len(arr)-1):
        if arr[i] == 0:
            arr.remove(0)
            arr.append(0)
    return arr

print(moveZeros([0,1,0,3,12]))