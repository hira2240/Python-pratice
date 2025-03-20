def INCREMENT(A, k):
    i = 0
    while i < k and A[i] == 1:
        A[i] = 0
        i = i + 1
    if i < k:
        A[i] = 1
    return A

# Example usage:
A = [1, 0, 1]  # Represents the binary number '101' (5 in decimal)
k = len(A)
# Increment the binary number by 1
new_A = INCREMENT(A, k)
print(new_A)  # Should output [0, 1, 1] which is '110' (6 in decimal)