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
    arr.append(y)

arr.sort()
print(arr[0] + arr[-1])
    

# 1 2 9 100 -> 뭘해도 C가 101 -> 맨 앞이랑 맨뒤
# 1 1 9 10 -> 뭘해도 11 -> 맨 앞이랑 뒤