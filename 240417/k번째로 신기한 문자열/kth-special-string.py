N, K, T = map(str, input().split())
N = int(N)
K = int(K)
l = len(T)

arr = []
for _ in range(N):
    word = input()
    if len(word) >= l and word[:l] == T:
        arr.append(word)

arr.sort()
print(arr[K-1])