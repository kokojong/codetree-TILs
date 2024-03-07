# a ~ f -> 각각 1~4
from collections import deque

inputs = list(input())

arr = []
word = []

def DFS():
    global arr

    if len(word) == 6:
        arr.append(word.copy())
        return

    for i in range(1, 5):
        word.append(i)
        DFS()
        word.pop()

DFS()

answer = 0

for alphas in arr:
    dic = dict()
    dic["a"] = alphas[0]
    dic["b"] = alphas[1]
    dic["c"] = alphas[2]
    dic["d"] = alphas[3]
    dic["e"] = alphas[4]
    dic["f"] = alphas[5]

    # print("dict", dic)
    def convert(k):
        if k not in ["+", "-", "*"]:
            return str(dic[k])
        else:
            return k

    queue = deque()
    for i in inputs:
        queue.append(convert(i))

    # print("queue", queue)
    
    while len(queue) > 2:
        x = int(queue.popleft())
        op = queue.popleft()
        y = int(queue.popleft())

        # print(x, op, y)
        if op == '+':
            result = x+y
        elif op == '-':
            result = x-y
        elif op == "*":
            result = x*y
        
        queue.appendleft(result)
    
    answer = max(queue[0], answer)

print(answer)