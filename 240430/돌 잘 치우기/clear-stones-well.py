from itertools import combinations
from collections import deque
import copy
N, K, M = map(int, input().split())

board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)
# print(board)
rocks = []
for r in range(N):
    for c in range(N):
        if board[r][c] == 1:
            rocks.append([r, c])

queue = deque()
for _ in range(K):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    queue.append((r, c))

def BFS(board):
    visited = [[False for _ in range(N)] for _ in range(N)]
    q = copy.deepcopy(queue)
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]

    while q:
        qr, qc = q.popleft()
        visited[qr][qc] = True
        
        for i in range(4):
            rr = qr + dr[i]
            cc = qc + dc[i]

            if 0<=rr<N and 0<=cc<N and visited[rr][cc] == False and board[rr][cc] == 0:
                q.append((rr, cc))
                visited[rr][cc] = True
    # print(visited)
    result = 0
    for r in range(N):
        for c in range(N):
            if visited[r][c]:
                result += 1
    return result

answer = 0
for posible in combinations(rocks, M):
    newBoard = copy.deepcopy(board)
    for posi in list(posible):
        newBoard[posi[0]][posi[1]] = 0
    answer = max(BFS(newBoard), answer)
print(answer)