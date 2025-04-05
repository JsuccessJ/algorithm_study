# 주어진 행렬들을 가장 최소의 횟수로 곱해야 한다.
# 행렬 A(3*2), B(2*4), C(4*3) 이 순서대로 주어 질 때 이를 곱하는 방법은 두가지 이다.

# (A*B) * C
# A * (B*C)

# 첫 번째 방법에서 총 곱셈 수는 (3*2*4) + (3*4*3) = 60 번이다. 
# 두 번째 방법은 (2*4*3) + 3*2*3 = 36 이다. 따라서 두번째 방법으로 행렬을 곱해야한다.
# 여러분이 할일은 N개의 행렬를 모두 곱하는데 드는 최소 횟수를 구하는 것이다.

# Input Format
# 첫째줄에 연산을 수행할 행렬 n(1<=n<=100)을 입력받는다.
# 두번째줄부터 n개의 행렬의 행 col(1<=col<=100)과 열 row(1<=row<=100)를 공백을 사이에 두고 입력받는다.

# Output Format
# 행렬연산의 최소 횟수를 출력한다.

def matrixChain(n):
    m = [[0] * (n+1) for _ in range(n+1)]
    for r in range(1, n):
        for i in range(1, n-r+1):
            j = i+r
            m[i][j] = min(m[i][k] + m[k+1][j] + p[i-1][0]*p[k-1][1]*p[j-1][1] for k in range(i, j))
    return m[1][n]

n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]
print(matrixChain(n))
