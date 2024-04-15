N = int(input())

A = 0
B = 0
win = -1 # -1: 둘다 이김 1: A가 이김, 0: B가 이김
answer = 0

for _ in range(N):
    c, s = input().split()
    s = int(s)
    if c == "A":
        A += s
    else:
        B += s
    
    if A > B: # 이기고 있는 사람 -> A가 이긴다면 1
        newWin = 1
    elif A == B:
        newWin = -1
    else:
        newWin = 0
    
    if win != newWin:
        answer += 1
    
    win = newWin

print(answer)