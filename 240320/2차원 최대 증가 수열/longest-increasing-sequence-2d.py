R, C = map(int, input().split())

board = []
for _ in range(R):
    row = list(map(int, input().split()))
    board.append(row)

# 0, 0 에서 시작
# 점프: 현재 위치의 적힌 수보다 점프한 이후가 더 커야함
# 점프시 오른쪽 + 아래쪽에 있는 위치로만 점프가 가능

dp = [[0 for _ in range(C)] for _ in range(R)]
# 0,0 부터 일단 시작해두기

for r in range(1, R):
    for c in range(1, C):
        if board[r][c] > board[0][0]:
            dp[r][c] = 1

# print(dp)

for r in range(1, R):
    for c in range(1, C):
        # 시작점
        for rr in range(r+1, R):
            for cc in range(c+1, C):
                if board[rr][cc] > board[r][c]:
                    dp[rr][cc] = max(dp[r][c] + 1, dp[rr][cc])

# print(dp)
answer = 0
for d in dp:
    answer = max(max(d), answer)
print(answer+1)