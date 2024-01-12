n, m = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

arr = A + B
arr.sort()

print(*arr)