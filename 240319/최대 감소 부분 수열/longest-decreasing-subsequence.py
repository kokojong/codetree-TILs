N = int(input())

arr = list(map(int, input().split()))

dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))