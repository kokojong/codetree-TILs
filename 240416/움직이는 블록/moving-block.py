# from coll
N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))

T = sum(arr)//N

answer = 0
while arr.count(T) < N:
    arr.sort()
    
    diff = T - arr[0] # 최솟값과 목표값의 차이를 구함 
    diff_max = abs(T - arr[-1])
    arr[0] += diff # 그 차이만큼 최솟값에 더해줌
    arr[-1] -= diff_max # 그 차이만큼 최댓값을 빼줌

    # print(arr)
    answer += diff

print(answer)