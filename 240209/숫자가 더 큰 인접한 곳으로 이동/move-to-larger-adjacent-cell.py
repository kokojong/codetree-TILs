N, r, c = map(int, input().split())

r -= 1
c -= 1

board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

answer = [board[r][c]]

while True:
    next = []

    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]
        
        if 0<=rr<N and 0<=cc<N and board[rr][cc] > board[r][c]:
            next.append((board[rr][cc], rr, cc, i))

    next.sort(key = lambda x: (x[3]))

    if next:
        answer.append(next[0][0]) # 숫자
        r, c = next[0][1], next[0][2]
    else:
        break
    
print(*answer)