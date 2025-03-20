from array import *

def count_inversion(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                count += 1
    print(count)
count_inversion([3, 2, 8, 11, 1, 0, 7])