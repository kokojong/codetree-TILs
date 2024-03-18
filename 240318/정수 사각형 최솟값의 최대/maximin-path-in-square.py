N = int(input())

board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

dp = [[0 for _ in range(N)] for _ in range(N)]

# 거기에 적혀있는 숫자들 중 최솟값을 최대로

dp[0][0] = board[0][0]

for c in range(1, N):
    dp[0][c] = min(dp[0][c-1], board[0][c])

for r in range(1, N):
    dp[r][0] = min(dp[r-1][0], board[r][0])

for r in range(1, N):
    for c in range(1, N):
        dp[r][c] = min(max(dp[r-1][c], dp[r][c-1]), board[r][c])

print(dp[-1][-1])