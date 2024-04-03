// 1번과 N번 이외에 한개씩 건너뛰어보고 하기
// 거리 - |x1-x2| + |y1-y2|

let N = Int(readLine()!)!

var arr: [[Int]] = []

for _ in 0..<N {
    let input = readLine()!.split(separator: " ").map { Int(String($0))! }
    arr.append(input)
}

var results: [Int] = [] // i번과 i+1번을 연결한 것들의 길이 모음
var total = 0
var answer: Int = Int.max

for i in 0..<N-1 {
    let x1 = arr[i][0]
    let y1 = arr[i][1]

    let x2 = arr[i+1][0]
    let y2 = arr[i+1][1]

    let result = abs(x1 - x2) + abs(y1 - y2)
    results.append(result)
    total += result
}

for i in 1..<N-1 { // i번을 건너 뛴 경우
    let t = total - results[i-1] - results[i] // i-1 ~ i, i ~ i +1 의 길이를 빼줌

    let x1 = arr[i-1][0]
    let y1 = arr[i-1][1]

    let x2 = arr[i+1][0]
    let y2 = arr[i+1][1]
    let result = abs(x1 - x2) + abs(y1 - y2)

    answer = min(t + result, answer)
}

print(answer)