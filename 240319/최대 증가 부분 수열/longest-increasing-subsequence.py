N = int(input())

arr = list(map(int, input().split()))

dp = [1 for _ in range(N)] # i번쨰 입장에서 바라보기 -> 내 앞에서 돌면서 나보다 작은애가 있을때 dp 갱신

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))