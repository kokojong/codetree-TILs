N = int(input())

M = 0

arr = []
for _ in range(N):
    s, e, p = map(int, input().split())
    arr.append((s, e, p))

dp = [0 for _ in range(N)]
dp[0] = arr[0][2] # p

for i in range(1, N):
    s,e,p = map(int, arr[i])

    for j in range(i):
        if j > e:
            dp[i] = max(dp[j] + p, dp[i])
        else:
            dp[i] = max(p, dp[i])

print(max(dp))
# print(dp[-1])