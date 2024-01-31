R, C = map(int, input().split())

board = []

for _ in range(R):
    row = list(map(int, input().split()))
    board.append(row)

answer = [-1]

for r in range(R):
    for c in range(C):

        # r ~ rr
        # c ~ cc
        for rr in range(r, R):
            for cc in range(c, C):
                flag = True

                for rrr in range(r, rr+1):
                    for ccc in range(c, cc+1):
                        if board[rrr][ccc] <= 0:
                            flag = False
                
                # print(flag, (r, c), (rr, cc))
                if flag:
                    answer.append((rr-r+1) * (cc-c+1))

print(max(answer))