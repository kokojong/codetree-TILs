N = int(input())

arr = list(map(int, input().split()))

# 최대 점프 가능 거리

dp = [0 for _ in range(N)]

# i에서부터 뒤로 가면서 하나씩 살펴보고 +1 되는지 확인하기??

for i in range(N):
    k = arr[i] # 최대 k만큼 점프할 수 있음

    for j in range(1,k+1):
        if i+j < N:
            dp[i+j] += 1
    
answer = 0
# print(dp)
for i in range(1, N):
    answer = max(dp[i], answer)
    if dp[i] == 0:
        break
    # else:
    #     answer = max(dp[i], answer)

print(answer)