N = int(input())

board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

dp = [[1 for _ in range(N)] for _ in range(N)] # 이 지점부터 이동이 가능한 최대 거리

dr = [-1, 0, 1 ,0]
dc = [0, 1, 0, -1]

cells = []
for r in range(N):
    for c in range(N):
        cells.append((board[r][c], r, c))

cells.sort()

# print(cells)

for k, r, c in cells:
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]

        if 0<=rr<N and 0<=cc<N and board[r][c] < board[rr][cc]:
            dp[rr][cc] = max(dp[r][c] + 1, dp[rr][cc])

answer = 0
for d in dp:
    answer = max(max(d), answer)
print(answer)

# for i in range(N):
#     for j in range(N):