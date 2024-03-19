N = int(input())

arr = list(map(int, input().split()))

# 최대 점프 가능 거리

dp = [-1 for _ in range(N)]

# i에서부터 뒤로 가면서 하나씩 살펴보고 +1 되는지 확인하기??

dp[0] = 0

for i in range(N):
    for j in range(i):
        if j + arr[j] >= i:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))