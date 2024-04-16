from collections import defaultdict

N, K = map(int, input().split())
arr = list(map(int, input().split()))

dic = defaultdict(int)

for a in arr:
    dic[a] += 1

# print(dic)

answer = 0
for k in set(arr):
    v = dic[k]
    k2 = K-k
    if k == k2:
        result = v*(v-1)
    else:
        result = v * dic[k2]
    answer += result

print(answer//2)