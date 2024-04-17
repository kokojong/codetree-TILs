N = int(input())

board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

visited = [[False for _ in range(N)] for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

def DFS(r, c):
    global visited

    stack = [[r, c]]
    visited[r][c] = True
    result = 0

    while stack:
        qr, qc = stack.pop()
        result += 1

        for i in range(4):
            rr = qr + dr[i]
            cc = qc + dc[i]

            if 0<=rr<N and 0<=cc<N and board[rr][cc] == 1 and visited[rr][cc] == False:
                stack.append([rr, cc])
                visited[rr][cc] = True
    
    return result

answer = []
for r in range(N):
    for c in range(N):
        if board[r][c] == 1 and visited[r][c] == False:
            l = DFS(r,c)
            answer.append(l)

answer.sort()

print(len(answer))
for a in answer:
    print(a)