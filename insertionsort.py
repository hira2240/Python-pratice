def insertionsort(A):
    n = len(A)
    i = 2
    for i in range(1, n):
        j = i
        while (j > 0 and A[j-1] > A[j]):
            A[j-1], A[j] = A[j], A[j-1]
            j -= 1
    return A

A = [5, 4, 3, 2, 1]
print("sorted list:", insertionsort(A))