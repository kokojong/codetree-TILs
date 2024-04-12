N = int(input())

arr = list(map(int, input()))

last = 0
dis = []
for i in range(1, N):
    if arr[i] == 1:
        dis.append(i - last)
        last = i

# print(dis)
print((max(dis)) // 2)

# 17
# 10001001000100001
# 2