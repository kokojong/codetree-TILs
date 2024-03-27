N = int(input())

M = 0

arr = []
for _ in range(N):
    s, e, p = map(int, input().split())
    arr.append((s, e, p))
    M = max(e, M)

dp = [0 for _ in range(M+1)]

for s,e,p in arr:
    for i in range(e, M+1):
        dp[i] = max(dp[s-1] + p, dp[i])

print(dp[-1])