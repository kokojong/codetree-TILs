N = int(input())
board = []

for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

# 방향 - 위 오 아 왼
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

answer = 0

def simulate(r, c, d): # r, c 에서 시작하며 방향이 d
    global answer

    cnt = 1

    while True:
        if 0<=r<N and 0<=c<N:
            if board[r][c] == 1:
                if d == 0:
                    d = 1
                elif d == 1:
                    d = 0
                elif d == 2:
                    d = 3
                elif d == 3:
                    d = 2
            elif board[r][c] == 2:
                if d == 0:
                    d = 3
                elif d == 1:
                    d = 2
                elif d == 2:
                    d = 1
                elif d == 3:
                    d = 0

            rr = r + dr[d]
            cc = c + dc[d]

            # print("r, c", r, c, rr, cc)

            r = rr
            c = cc
            cnt += 1
        else:
            answer = max(answer, cnt)
            return cnt # 밖으로 나간거라면 cnt return


for i in range(N):
    simulate(N-1, i, 0)
    simulate(i, 0, 1)
    simulate(0, i, 2)
    simulate(i, N-1, 3)
    
# print(simulate(1, 2, 3))

print(answer)