n, m = map(int, input().split())

board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

answer = 0

for r in range(n): # 행에서 먼저 체크
    for c in range(0, n-m+1):
        if len(set(board[r][c:c+m])) == 1:
            answer += 1
            continue

for c in range(n):
    tmp = []
    for r in range(0, n):
        tmp.append(board[r][c])
    
    for i in range(0, n-m):
        if len(set(tmp[i:i+m])) == 1:
            answer += 1
            continue
print(answer)