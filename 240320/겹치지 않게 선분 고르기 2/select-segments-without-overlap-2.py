N = int(input())

arr = []
for _ in range(N):
    x1, x2 = map(int, input().split())
    arr.append((x1, x2))

# print(arr)
arr.sort()

dp = [0 for _ in range(1001)] # 최대 위치가 1000
# dp[i]로 끝나는 선분?

for a, b in arr:
    k = max(dp[:a])
    
    for i in range(a, b+1):
        dp[i] = max(k+1, dp[i])

print(max(dp))