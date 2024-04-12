N = int(input())

arr = list(map(int, input()))

last = 0
dis = []
for i in range(N):
    if arr[i] == 1:
        dis.append((i - last + 1) // 2)
        last = i

# print(dis)
print(max(dis))