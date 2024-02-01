# 길이가 n인 문자열 A
# 오른쪽으로 shift하고 인코딩 했을떄의 길이가 최소가 되도록 하기

from collections import deque

arr = deque(list(input().rstrip()))
n = len(arr)

answer = n * 2

for _ in range(n):
    arr.appendleft(arr.pop())

    arr_list = list(arr)

    result = ""

    last = arr_list[0]
    cnt = 1

    for i in range(1, n):
        if arr_list[i] == last:
            cnt += 1
        else:
            result += last
            result += str(cnt)

            last = arr_list[i]
            cnt = 1
    
    if cnt > 0:
        result += last
        result += str(cnt)

    answer = min(answer, len(result))

print(answer)