R, C = map(int, input().split())

board = []
for _ in range(R):
    row = list(map(int, input().split()))
    board.append(row)

visited = [[False for _ in range(C)] for _ in range(R)]
# dfs 3개로 해서 풀기

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

answer = 0

def dfs(r, c, s, l):
    global answer
    if l == 3:
        # print("s", s)
        answer = max(answer, sum(s))
        return

    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]

        if 0<=rr<R and 0<=cc<C and not visited[rr][cc]:
            visited[rr][cc] = True
            dfs(rr, cc, s+[board[rr][cc]], l+1)
            visited[rr][cc] = False
    

for r in range(R):
    for c in range(C):
        visited[r][c] = True
        dfs(r, c, [board[r][c]], 1)
        visited[r][c] = False
print(answer)