# 세수를 더했을 때 K가 되는 조합의 갯수

# 두개를 더한걸 하나의 딕셔너리로 만들고 이거랑 나머지 1개 처리하기

from collections import defaultdict

N, K = map(int, input().split())

arr = list(map(int, input().split()))

dic = defaultdict(int)

# 변수 선언 및 입력:
# count = dict()

# ans = 0
# # 배열을 앞에서부터 순회하며 쌍을 만들어줍니다.
# for elem in arr:
#     diff = k - elem
#     # 가능한 모든 쌍의 수를 세어줍니다.
#     if diff in count:
#         ans += count[diff]

#     # 현재 숫자의 개수를 하나 증가시켜줍니다.
#     if elem in count:
#         count[elem] += 1
#     else:
#         count[elem] = 1

# print(ans)

# 한개 고른거로 치기
for a in arr:
    dic[a] += 1

# print(dic)
answer = 0
three = False
for i in range(N):
    for j in range(i+1, N):
        a = arr[i]
        b = arr[j]
        s = a + b # 두개를 더한거
        c = K - s # dic[c]가 존재하는지 확인해야함
        
        result = 0
        if c == a and c == b: # 세개 다 같은거
            # result = dic[c] * (dic[c]-1) * (dic[c] - 2) # 그중에서 3개 고르기 - 0 될수도 있음
            three = True
        elif c == a and dic[c] > 1:
            result = dic[c]-1
        elif c == b:
            result = dic[c]-1
        else: # 겹치는게 없는거
            result = dic[c]
        # print("a, b, c", a, b, c, result)
        answer += result

answer = answer//3
if three:
    # print("k//3", K//3, dic[K//3])
    answer += (dic[K//3] * (dic[K//3]-1) * (dic[K//3]-2))//6

print(answer)