N = int(input())

board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

dp = [[0 for _ in range(N)] for _ in range(N)]

# 왼쪽 혹은 밑으로만 이동

dp[0][-1] = board[0][-1]

for c in range(N-2, -1, -1):
    dp[0][c] = dp[0][c+1] + board[0][c]

for r in range(1, N):
    dp[r][-1] = dp[r-1][-1] + board[r][-1]

# print(dp)

for r in range(1, N):
    for c in range(N-2, -1, -1):
        dp[r][c] = min(dp[r-1][c], dp[r][c+1]) + board[r][c]

print(dp[-1][0])