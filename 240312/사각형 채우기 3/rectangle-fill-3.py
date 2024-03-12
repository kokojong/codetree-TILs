n = int(input())

dp = [1 for _ in range(n+1)]

dp[1] = 2
if n == 1:
    print(dp[-1])
    exit()
dp[2] = 7
if n == 2:
    print(dp[-1])
    exit()

dp[3] = dp[1]*3 + dp[2]*2 + dp[0] * 2
for i in range(3, n):
    dp[i] = dp[i-1] * 3 + dp[i-2] *2 + dp[i-3] * 2
    dp[i] %= 1_000_000_007

print(dp[-1])