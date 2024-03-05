N = int(input())

board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

bombs = [
    [(-2, 0), (-1, 0), (1, 0), (2, 0)],
    [(-1, 0), (1, 0), (0, 1), (0, -1)],
    [(-1, -1), (-1, 1), (1, -1), (1, 1)]
]

positions = []

for r in range(N):
    for c in range(N):
        if board[r][c]:
            positions.append((r, c))

cnt = len(positions) # 폭탄의 갯수

# bomb를 [0, 1, 2] 라고 생각하고 각각 해보기

stack = []

answer = 0

def simulate():
    global answer

    if len(stack) == cnt:
        
        visited = [[0 for _ in range(N)] for _ in range(N)]

        for i in range(cnt):
            r, c = positions[i]
            visited[r][c] = 1
            
            k = stack[i]

            for j in range(4):
                rr = r + bombs[k][j][0]
                cc = c + bombs[k][j][1]

                if 0 <= rr < N and 0 <= cc < N:
                    visited[rr][cc] = 1
        
        # print("visited", visited)
        result = 0
        for i in range(N):
            result += sum(visited[i])

        answer = max(result, answer)

        return

    for i in [0, 1, 2]:
        stack.append(i)
        simulate()
        stack.pop()

simulate()

print(answer)