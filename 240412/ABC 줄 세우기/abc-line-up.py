N = int(input())
arr = list(map(str, input().split())) 

target = sorted(arr)

# print(arr)
# print(target)

answer = 0

for i in range(N):
    j = i
    # print(arr[i], target[i])
    while arr[i] != target[i] and j < N-1:
        tmp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = tmp
        answer += 1
        j += 1

print(answer)