from collections import deque

n, t = map(int, input().split())

t %= (3*n)
arr = deque()

for _ in range(3):
    for a in map(int, input().split()):
        arr.append(a)

for i in range(t):
    # arr.append(arr.popleft())
    arr.appendleft(arr.pop())

arr = list(arr)
for i in range(3):
    print(*arr[n*i:n*(i+1)])