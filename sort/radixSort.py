n = int(input())
arr = list(map(int, input().split()))
numDigits = 0

def radixSort(A, n, k):
    for digit in range(1, k+1):
        cnt = [0] * 10
        start = [0] * 10
        B = [0] * (n+1)
        for i in range(0, n):
            cnt[A[i]//10**(digit-1)%10] += 1
        for d in range(1, 10):
            start[d] = start[d-1] + cnt[d-1]
        for j in range(0, n):
            start[A[j]//10**(digit-1)%10] += 1
            B[start[A[j]//10**(digit-1)%10]] = A[j]
        A = B[1 : n+1]
    return A

for i in range(n):
    if numDigits < arr[i]: numDigits = arr[i]

numDigits = len(str(numDigits))
print(radixSort(arr,n,numDigits))
