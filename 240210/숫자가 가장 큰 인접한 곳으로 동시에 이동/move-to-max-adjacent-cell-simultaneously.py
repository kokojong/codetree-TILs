# 상하좌우
# 만약에 겹치면 구슬이 서로 사라짐

N, M, T = map(int, input().split()) # 크기, 구슬수, 시간

board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

balls = []
ballBoard = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c = map(int, input().split())
    balls.append((r-1, c-1))
    ballBoard[r-1][c-1] += 1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while T:
    T -= 1
    
    ballBoard = [[0 for _ in range(N)] for _ in range(N)]

    for r, c in balls:
        posibles = []
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]

            if 0<=rr<N and 0<=cc<N:
                posibles.append((board[rr][cc], rr, cc, i)) # 값, 위치, 방향
        posibles.sort(key = lambda x: (-x[0], x[3]))
        # print("p", posibles)
        rrr, ccc = posibles[0][1], posibles[0][2]
        ballBoard[rrr][ccc] += 1

    # print("ballBoard", ballBoard)

    balls = []
    for i in range(N):
        for j in range(N):
            if ballBoard[i][j] > 1:
                ballBoard[i][j] = 0
            elif ballBoard[i][j] == 1:
                balls.append((i, j))

# print("ballBoard", ballBoard)
answer = 0
for i in range(N):
    for j in range(N):
        if ballBoard[i][j]:
            answer += 1
print(answer)