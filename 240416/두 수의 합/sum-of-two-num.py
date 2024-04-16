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
    # print(k, v)
    result = v * dic[K-k]
    answer += result

print(answer//2)