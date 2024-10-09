n = int(input())
arr = list(map(int, input().split()))
max = 0

def countingSort(A):
    C = [0] * (max+1)
    B = [0] * n
    for j in range(0, n):
        C[A[j]] += 1
    for i in range(1, max+1):
        C[i] += C[i-1]
    for j in range(n-1, -1, -1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1
    return B

for i in range(n):
    if max < arr[i]: max = arr[i]

print(countingSort(arr))
