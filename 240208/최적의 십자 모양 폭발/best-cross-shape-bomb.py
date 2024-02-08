# 선택한 숫자만큼 상하좌우로 터진다
# 터트리고나서 중력에 의해 애들이 내려옴

# 목표: 격자끼리 적혀있는 숫자가 동일한 쌍이 최대가 되도록
# -> 체크하는 메서드 필요할듯

# 가능한 경우의 수 -> N*N 에서 1개를 골라서 터트림 -> 완탐

# import copy

# N = int(input())

# board = []

# for _ in range(N):
#     row = list(map(int, input().split()))
#     board.append(row)

# def bomb(r, c, newBoard):
#     k = newBoard[r][c]-1
#     newBoard[r][c] = 0

#     for rr in range(r-k, r+k+1):
#         if 0<=rr<N:
#             newBoard[rr][c] = 0

#     for cc in range(c-k, c+k+1):
#         if 0<=cc<N:
#             newBoard[r][cc] = 0

#     # print("터진상태", newBoard)

#     for i in range(N-1, -1, -1):
#         for j in range(N):
#             if newBoard[i][j] == 0 and i-1 >= 0:
#                 newBoard[i][j] = newBoard[i-1][j]
#                 newBoard[i-1][j] = 0

#     # print("중력 적용", newBoard)
                
#     return newBoard

# def checkBoard(newBoard):
#     cnt = 0
#     for r in range(N):
#         for c in range(N):
#             if newBoard[r][c] == 0:
#                 continue
#             # 아래꺼랑 비교하기
#             if r+1 < N:
#                 if newBoard[r][c] == newBoard[r+1][c]:
#                     cnt += 1
#             # 오른쪽거랑 비교하기
#             if c+1 < N:
#                 if newBoard[r][c] == newBoard[r][c+1]:
#                     cnt += 1
#     return cnt

# answer = 0
# for r in range(N):
#     for c in range(N):
#         new = bomb(r, c, copy.deepcopy(board))
#         result = checkBoard(new)
#         # print(result, r, c, new)
#         answer = max(answer, result)
# print(answer)

# new = bomb(2, 1, copy.deepcopy(board))
# print(new)
# print(checkBoard(new))
# for r in range(N):
#     print(*new[r])
# print()


# 4
# 1 1 2 1 
# 1 2 1 1 
# 1 2 1 2 
# 1 1 1 2

# 정답 12, 내 답 11 ???

import copy


n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))


def bomb(i,j,temp):
    bo = temp[i][j]
    temp[i][j] = 0
    #print('-----')
    #print(bo)
    for x in range(0,bo):
        #print(x)
        if j+x < n :
            temp[i][j+x] = 0
        if i+x < n :
            temp[i+x][j] = 0
        if i-x >= 0 :
            temp[i-x][j] = 0
        if j-x >= 0 :
            temp[i][j-x] = 0
    return temp

def check(temp):
    temp_new  = []
    #temp_new2 = [[ ]for _ in range(n)]
    temp_new2 = [[] for _ in range(n)]

    for i in range(n):
        new = []
        for j in range(n):
            if temp[j][i] != 0 :
                new.append(temp[j][i])

        if len(new) < n :
            for k in range(n - len(new)):
                new.insert(0,0)
        
        temp_new.append(new)

    for j in range(n):
        
        for i in range(n):
        
            temp_new2[j].append(temp_new[i][j])

    return temp_new2



ans = 0
for i in range(n):
    for j in range(n):
        # arr[i][j] 터트리기
        #print('------')
        #print(arr)
        temp = copy.deepcopy(arr)
        temp2 = bomb(i,j, temp)
        after_bomb = check(temp2)

        # 개수 세기
        
        cnt = 0
        for k in range(1,n):
            for m in range(1,n):
                if after_bomb[k][m] != 0 :
                    if after_bomb[k][m] == after_bomb[k][m-1] :
                        cnt += 1
                    if after_bomb[m][k] == after_bomb[m-1][k] :
                        cnt += 1
        ans = max(ans,cnt)
        #print(after_bomb, cnt)

print(ans)