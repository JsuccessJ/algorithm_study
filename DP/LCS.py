# 염기서열의 종류가 너무 많아 비교하기가 어려워 LCS(최장공통부분순서) 알고리즘을 사용하기로 하였다.
# 이 문제에서는 동적프로그래밍을 이용해 두개의 염기서열을 비교하여 LCS 길이를 출력하는 프로그램을 짜보도록 한다.

# Input Format
# 비교하고자 하는 두 염기서열 a, b를 입력 받는다. 염기서열 a,b={'a'...'z'}

# Output Format
# 주어진 두 문자열의 LCS길이를 출력한다.

# Sample Input
# aabccqww
# qwwaqwwb

# Sample Output
# 4

def LCS(m, n):
    C = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]: C[i][j] = C[i-1][j-1]+1
            else: C[i][j] = max(C[i-1][j], C[i][j-1])
    return C[m][n]

a = input()
b = input()
print(LCS(len(a), len(b)))
