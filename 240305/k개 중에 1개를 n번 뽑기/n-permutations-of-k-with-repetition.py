# 1이상 K이하를 N번해서 나올수 있는 모든 순서쌍

K, N = map(int, input().split())

nums = [i for i in range(1, K+1)]

word = []

def recursive():
    if len(word) == K:
        print(*word)
        return

    for n in nums:
        word.append(n)
        recursive()
        word.pop()

recursive()