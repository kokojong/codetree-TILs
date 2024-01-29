N = int(input())

board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

answer = 0
for r in range(0, N-2):
    for c in range(0, N-2):
        cnt = 0
        for i in range(3):
            for j in range(3):
                cnt += board[r+i][c+j]
        # print("cnt", cnt)
        answer = max(answer, cnt)

print(answer)