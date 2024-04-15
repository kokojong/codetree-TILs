# 가능한거: -, 0, + 의 배열 만들어서 sort

N = int(input())
arr = list(map(int, input().split()))

minus = []
plus = []
zero = []

for a in arr:
    if a > 0:
        plus.append(a)
    elif a < 0:
        minus.append(a)
    else:
        zero.append(a)

minus.sort()
plus.sort()
zero.sort()

answer = -float('inf')

# 가능: 플러스 3, 마2 플1, 0 있으면 0처리, 그래도 진짜 없으면 -에서 가장 큰거 3개

if len(plus) >= 3:
    answer = max(plus[-1] * plus[-2] * plus[-3] ,answer)

if len(minus) >= 2 and len(plus) >= 1:
    answer = max(minus[0] * minus[1] * plus[-1], answer)

if len(minus) >= 3:
    answer = max(minus[-1] * minus[-2] * minus[-3] , answer)

if len(minus) >= 1 and len(plus) >= 2:
    answer = max(minus[-1] * plus[-1] * plus[-2], answer)

if len(zero) > 0:
    answer = max(0, answer)

print(answer)