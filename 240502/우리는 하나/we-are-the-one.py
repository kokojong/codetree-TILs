from itertools import combinations
from collections import deque

N, K, U, D = map(int, input().split())

board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

rc = []
for r in range(N):
    for c in range(N):
        rc.append([r, c])

answer = 0 

posibles = combinations(rc, K)
for posible in list(posibles):
    
    visited = [[False for _ in range(N)] for _ in range(N)]
    for r, c in posible:
        visited[r][c] = True

    queue = deque(posible)
    
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]
    
    cnt = len(queue)

    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]

            if 0<=rr<N and 0<=cc<N and visited[rr][cc] == False:
                diff = abs(board[rr][cc] - board[r][c])
                if U<=diff<=D:
                    
                    visited[rr][cc] = True
                    cnt += 1
                    queue.append([rr, cc])

    answer = max(cnt, answer)

print(answer)