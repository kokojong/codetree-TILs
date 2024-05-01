from collections import deque

R, C = map(int, input().split())

board = []
for _ in range(R):
    row = list(map(int, input().split()))
    board.append(row)


total = 0
for r in range(R):
    for c in range(C):
        if board[r][c] == 1:
            total += 1
time = 0

def BFS():
    global board

    visited = [[False for _ in range(C)] for _ in range(R)]
    queue = deque()
    queue.append([0, 0]) # 무조건 물이니까
    visited[0][0] = True
    
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]

    ices = []

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]

            if 0<=rr<R and 0<=cc<C and visited[rr][cc] == False:
                if board[rr][cc] == 1:
                    ices.append([rr, cc])
                else:
                    queue.append([rr, cc])
                
                visited[rr][cc] = True
    
    # print(ices)

    for r, c in ices:
        board[r][c] = 0

    return len(ices)

while total > 0:
    result = BFS()
    # print("board", board, result)
    total -= result
    time += 1

print(time, result)