N = int(input())
arr = list(map(str, input().split())) 

target = sorted(arr)

# print(arr)
# print(target)

answer = 0

for i in range(N):
    if arr[i] == target[i]:
        continue

    for j in range(i, N-1):
        arr[j], arr[j+1] = arr[j+1], arr[j]
        answer += 1

        if arr[i] == target[i]:
            break

print(answer)