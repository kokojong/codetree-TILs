from collections import deque

# 행번호가 작은거, 열번호가 작은거 우선

N, K = map(int, input().split())
board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)
R, C = map(int, input().split())
R -= 1
C -= 1

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

def BFS(r, c): # 가능한 애들을 return 해주기

    global R
    global C

    T = board[r][c]
    queue = deque()
    posibles = [] # 숫자, r, c
    queue.append([r, c])

    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[r][c] = True

    while queue:
        qr, qc = queue.popleft()
        for i in range(4):
            rr = qr + dr[i]
            cc = qc + dc[i]

            if 0<=rr<N and 0<=cc<N and board[rr][cc] < T and visited[rr][cc] == False:
                queue.append([rr, cc])
                visited[rr][cc] = True
                posibles.append([board[rr][cc], rr, cc])

    posibles.sort(key = lambda x: (-x[0], x[1], x[2]))
    if len(posibles) > 0:
        p = posibles[0]
        R = p[1]
        C = p[2]

for _ in range(K):
    BFS(R, C)

print(R+1, C+1)