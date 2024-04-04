let NM = readLine()!.split(separator: " ").map { Int(String($0))! }
let N = NM[0]
let M = NM[1]

var board: [[Int]] = []
for _ in 0..<N {
    let row = readLine()!.split(separator: " ").map { Int(String($0))! }
    board.append(row)
}

// print(board)

var answer: [Int] = []
var dr = [-1, 0, 1, 0]
var dc = [0, -1, 0, 1]

func dfs(r: Int, c: Int, depth: Int, visited: [[Int]]) {
    if depth == 3 {
        answer.append(visited[r][c])
        return
    }

    var newVisited = visited

    for i in 0..<4 {
        let rr = r + dr[i]
        let cc = c + dc[i]

        if rr >= 0 && rr < N && cc >= 0 && cc < M && newVisited[rr][cc] == 0 {
            newVisited[rr][cc] = newVisited[r][c] + board[rr][cc]
            dfs(r: rr, c: cc, depth: depth+1, visited: newVisited)
        }
    }

}

for r in 0..<N {
    for c in 0..<M {
        var visited = Array(repeating: Array(repeating: 0, count: M), count: N)
        visited[r][c] = board[r][c]
        dfs(r: r, c: c, depth: 1, visited: visited)
    }
}
// print(answer)
answer.sort()
print(answer.last!)