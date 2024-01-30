# 채굴에 드는 비용: 마름모 격자의 갯수만큼
# 2k**2 + 2k + 1
# k = 1 -> 5
# k = 2 -> 4 + 9 = 13

# 금 한개가 m원일때

from collections import deque

N, M = map(int, input().split())

board = []

for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

def BFS(r, c, K): # r, c 에서 K의 크기만큼 bfs
    visited = [[False for _ in range(N)] for _ in range(N)]
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]

    queue = deque()
    queue.append((r, c, 0))
    visited[r][c] = True

    result = 0

    while queue:
        # print("queue", queue)
        qr, qc, qk = queue.popleft()

        if board[qr][qc]:
            result += 1
        
        for i in range(4):
            rr = qr + dr[i]
            cc = qc + dc[i]

            if 0<=rr<N and 0<=cc<N and (not visited[rr][cc]) and qk<K:
                queue.append((rr, cc, qk+1))
                visited[rr][cc] = True

    return result

answer = 0

for r in range(N):
    for c in range(N):
        for k in range(N+1): # 모든걸 감싸도록 하는걸 포함해야함
            result = BFS(r, c, k)
            # print(result, r, c, k)
            if result*M - (2*k*k + 2*k + 1) >= 0:
                answer = max(answer, result)

# print(BFS(2, 1, 1))

print(answer)