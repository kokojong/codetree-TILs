N = int(input())

board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

dp = [[1000000 for _ in range(N)] for _ in range(N)]

# 오른쪽 혹은 밑으로만
# 거쳐간 위치에 적혀있는 숫자들 중 최댓값을 최소로 하기

dp[0][0] = board[0][0]

for c in range(1, N):
    dp[0][c] = max(dp[0][c-1], board[0][c])

for r in range(1, N):
    dp[r][0] = max(dp[r-1][0], board[r][0])

# print(dp)

for r in range(1, N):
    for c in range(1, N):
        up = dp[r-1][c]
        left = dp[r][c-1]

        dp[r][c] = max(min(up, left), board[r][c])

# print(dp)
print(dp[-1][-1])

# 3
# 1 1 3
# 6 1 1
# 10 10 2