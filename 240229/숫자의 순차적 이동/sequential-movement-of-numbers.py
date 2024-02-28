N, M = map(int, input().split())

board = []

for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

# 8개중에서 가장 큰 숫자의 칸과 교환

arr = [[] for _ in range(N*N+1)] # i번의 위치

for r in range(N):
    for c in range(N):
        i = board[r][c]
        arr[i] = (r, c)

# print(arr)
 # 턴 한번이 16번을 옮기는것...!
while M:
    for k in range(1, 17):
        r, c = arr[k]

        posibles = []
        for i in range(8):
            rr = r + dr[i]
            cc = c + dc[i]

            if 0 <= rr < N and 0 <= cc < N:
                posibles.append((board[rr][cc], rr, cc))
        posibles.sort()
        n, rrr, ccc = posibles[-1]
        # print("posibles", posibles)

        # 원래 -> r, c에 k가 있음
        # 바꿀거 -> rrr, ccc에 n이 있음
        
        # 자리 바꿔주기
        board[rrr][ccc] = k
        board[r][c] = n

        # 자리 바꾼거 기입해주기
        arr[k] = (rrr, ccc)
        arr[n] = (r, c)

    # print("M-번째", M, board)

    M -= 1    

for i in range(N):
    row = board[i]
    print(*row)