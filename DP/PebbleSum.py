# 3*N 테이블의 각 칸에는 양 또는 음의 정수가 기록 되어 있다.
# "조약돌 놓기" 게임의 규칙은 다음과 같다.
# 1. 각 열에는 적어도 하나의 조약돌을 놓아야 한다
# 2. 가로나 세로로 인접한 두 칸에 동시에 조약돌을 놓을 수 없다.

# 문제의 목표는 조약돌이 놓인 자리의 모든 수를 더했을 때 그것이 최대가 되는 것을 구하는 것이다.
# 여러분이 할 일은 최대값을 구하는 프로그램을 작성하는 것이다.

# Input Format
# 첫 줄에는 보드판의 가로 크기 m (m<=100)이 들어온다.
# 그 다음 3줄에는 각 행의 원소값이 들어온다.

# Output Format
# 규칙에 맞게 조약돌을 놓고 그 합의 모든 경우의 수중 가장 큰 값을 출력한다.

def pebble(m):
    peb = [[0] * 4 for _ in range(m)]
    for i in range(m):
        for p in range(3):
            peb[i][p] = matrix[p][i]
        peb[i][3] = matrix[0][i] + matrix[2][i]
    for i in range(1, m):
        for p in range(4):
            if p == 3: k = peb[i-1][1]
            else: k = max(peb[i-1][j] for j in range(3+p%2) if p != j)
            peb[i][p] += k
    return max(peb[m-1][k] for k in range(4))

m = int(input())
matrix = [list(map(int, input().split())) for _ in range(3)]
print(pebble(m))
