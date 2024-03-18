N = int(input())

board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

dp = [[0 for _ in range(N)] for _ in range(N)]

# 오른쪽 또는 밑으로만

dp[0][0] = board[0][0]

for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            dp[i][j] = dp[i][j-1] + board[i][j]
        elif j == 0:
            dp[i][j] = dp[i-1][j] + board[i][j]
        else:
            dp[i][j] = max(dp[i-1][j] + board[i][j], dp[i][j-1] + board[i][j])

# print(dp)
print(dp[-1][-1])