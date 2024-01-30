# 1~n 으로 순서대로, 각각 Ai 명이 살고있음
# 한곳에 전부 모이려고 함!
# 모든 사람의 이동거리의 합이 최소

N = int(input())
arr = list(map(int, input().split()))

answer = float('inf')
for i in range(N):
    # 선택된 집: i
    result = 0
    for j in range(N):
        result += arr[j] * abs(i - j)

    answer = min(answer, result)

print(answer)