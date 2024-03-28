N, M = map(int, input().split())

arr = list(map(int, input().split()))

INF = float('inf')
dp = [0 for _ in range(M+1)] # 초기화
for i in range(1, M+1):
    if i%arr[0] == 0:
        dp[i] = i//arr[0]
# print(dp)

for i in range(1, N):
    K = arr[i]
    
    for j in range(1, M+1):
        if j >= K:
            dp[j] = min(dp[j-K] + 1, dp[j]) # K를 사용하지 않았을 때의 조건 + 1(사용)

    # print(dp)
print(dp[-1])