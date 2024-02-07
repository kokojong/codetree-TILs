# 선택한 숫자만큼 상하좌우로 터진다
# 터트리고나서 중력에 의해 애들이 내려옴

# 목표: 격자끼리 적혀있는 숫자가 동일한 쌍이 최대가 되도록
# -> 체크하는 메서드 필요할듯

# 가능한 경우의 수 -> N*N 에서 1개를 골라서 터트림 -> 완탐

import copy

N = int(input())

board = []

for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

def bomb(r, c, board):
    k = board[r][c]-1

    for rr in range(r-k, r+k+1):
        if 0<=rr<N:
            board[rr][c] = 0

    for cc in range(c-k, c+k+1):
        if 0<=cc<N:
            board[r][cc] = 0

    for r in range(N):
        for c in range(N):
            if r+1 < N and board[r+1][c] == 0:
                board[r+1][c] = board[r][c] # 내려 앉기
                board[r][c] = 0

    return board

def checkBoard(board):
    cnt = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == 0:
                continue
            # 아래꺼랑 비교하기
            if r+1 < N:
                if board[r][c] == board[r+1][c]:
                    cnt += 1
            # 오른쪽거랑 비교하기
            if c+1 < N:
                if board[r][c] == board[r][c+1]:
                    cnt += 1
    return cnt

answer = 0
for r in range(N):
    for c in range(N):
        new = bomb(r, c, copy.deepcopy(board))
        # print(new)
        result = checkBoard(new)
        # print(result)
        answer = max(answer, result)
print(answer)