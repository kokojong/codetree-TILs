# 1~C 번호가 매겨진 빨간돌
# 1~N 번호가 매겨진 검정돌

# 빨간돌에는 T가, 검정돌에는 A, B가 적혀있음
# A < T < B 가 되도록 1:1로 짝짓기하려고함
# 짝 지어지는게 최대 몇개나 가능한지

C, N = map(int, input().split())

red = []
for _ in range(C):
    red.append(int(input()))

black = []
for _ in range(N):
    black.append(list(map(int, input().split()))) # A ~ B

red.sort()
black.sort(key = lambda x: (x[0], x[1]-x[0]))

# print(red)
# print(black)

i = 0
j = 0
answer = 0

while i < C and j < N:
    if black[j][0] <= red[i] <= black[j][1]:
        i += 1
        j += 1
        answer += 1
        continue
    
    if black[j][1] < red[i]: # 구간보다 이미 넘어온거라면
        j += 1
        continue
    
    i += 1

# print("i, j", i, j)
print(answer)