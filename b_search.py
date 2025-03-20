def binary_search(A, lo, hi, x):
    if lo > hi:
        return None
    
    mid = (lo + hi) // 2
    
    if A[mid] == x:
        return mid 
    elif A[mid] < x:
        return binary_search(A, mid + 1, hi, x)
    else:
        return binary_search(A, lo, mid - 1, x)

A = [1, 2, 3, 4, 6, 6, 7, 8, 9, 10]
x = 2
result = binary_search(A, 0, len(A) - 1, x)

if result is not None:
    print(f"Element found at index {result}")
else:
    print("Element not found")
