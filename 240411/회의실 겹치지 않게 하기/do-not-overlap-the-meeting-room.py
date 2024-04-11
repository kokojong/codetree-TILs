N = int(input())

arr = []

for _ in range(N):
    s, e = map(int, input().split())
    arr.append([s, e])

arr.sort(key = lambda x: (x[1], -x[0]))

result = 1 # 동시에 가능한 갯수
end = arr[0][1]
for i in range(1, N):
    s, e = arr[i]
    if s >= end:
        result += 1
        end = e

print(N-result)