n = int(input())
arr = list(map(int, input().split()))

def radixSort(A, n, k):
    for digit in range(1, k+1):
        cnt = [0] * 10
        start = [0] * 10
        B = [0] * 10
        for i in range(0, n):
            cnt[A[i]//10**(digit-1)%10] += 1
        for d in range(1, 10):
            start[d] = start[d-1] + cnt[d-1]
        for i in range(0, n):
            start[A[i]//10**(digit-1)%10] += 1
            B[start[A[i]//10**(digit-1)%10]] = A[i]
        A = B[1 : n+1]
    return A

arr = radixSort(arr,n,3)
print(arr)
