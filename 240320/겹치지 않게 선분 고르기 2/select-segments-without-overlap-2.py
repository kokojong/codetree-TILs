N = int(input())

arr = []
for _ in range(N):
    x1, x2 = map(int, input().split())
    arr.append((x1, x2))

arr.sort(key = lambda x: (x[1], x[1]-x[0])) # 끝나는 점이 더 작고, 길이가 짧은 순으로 나열
# print(arr)

last = 0
answer = 0

for a, b in arr:
    if a > last:
        last = b
        answer += 1

print(answer)

# dp = [0 for _ in range(1001)] # 최대 위치가 1000
# # dp[i]로 끝나는 선분?

# for a, b in arr:
#     k = max(dp[:a])
    
#     for i in range(a, b+1):
#         dp[i] = max(k+1, dp[i])

# print(dp)
# print(max(dp))