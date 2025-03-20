A = [1, 2, 3, 4]
B = [4, 5, 6, 7]

n= len(A)

for i in range(n):
    B[i] = A[0]
    for j in range(1, i+1):
        B[i] = B[i] + A[j]
    B[i] = B[i] / (i+1)
print(B)

n = A.size 
failed = FALSE 
i = 1
while(i <= n and not failed):
    j = i+1
    while(j <= n and not failed):
        k = j+1
        while(k <= n and not failed):
            if(A[i] == A[j] or A[i]==A[k] or A[j] == A[k]):
                failed = TRUE 
            k = k+1
        j = j+1
    i = i+1
if (failed):
    return "fail"
else return "success"
