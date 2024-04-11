# 두개씩 짝지어주기. 두 자연수의 합이 가장 큰 두 자연수의 합을 C 일때 이거의 최솟값
# 평탄화를 해줘야함.

import heapq

N = int(input()) # M개의 자연수 중에서 서로 다른 값들의 갯수(Input 수)
M = 0

heap = []

# minV = float('inf')
# maxV = 0

arr = []
for _ in range(N):
    x, y = map(int, input().split()) # y가 x개 있다
    M += x
    arr.append([y, x])

arr.sort()

i = 0
j = N-1

answer = 0

while i < j:
    count = min(arr[i][1], arr[j][1]) # 이만큼 빼줄거임
    answer = max(arr[i][0] + arr[j][0], answer)
    arr[i][1] -= count
    if arr[i][1] == 0:
        i += 1
    
    arr[j][1] -= count
    if arr[j][1] == 0:
        j -= 1

# print("i, j", i, j, arr)

if i == j:
    answer = max(arr[i][0]*2, answer)

print(answer)