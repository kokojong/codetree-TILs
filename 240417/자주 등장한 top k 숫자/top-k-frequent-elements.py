from collections import defaultdict

N, K = map(int, input().split())

arr = list(map(int, input().split()))

dic = defaultdict(int)
for a in arr:
    dic[a] += 1

s = []
for (k, v) in dic.items():
    s.append([v, k])

s.sort(key = lambda x: (-x[0], -x[1]))

answer = []
for i in range(k):
    answer.append(s[i][1])

print(*answer)