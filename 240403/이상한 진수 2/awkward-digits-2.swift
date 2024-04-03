import Foundation

var b = Array(readLine()!).map { Int(String($0))! }
// var a = Array(readLine()!)

var answer: [Int] = []
for i in 0..<b.count {
    var tmp = b
    tmp[i] = (b[i]+1)%2
    let j = tmp.map{ String($0) }.joined(separator: "")
    // print(j)
    answer.append(Int(j,radix: 2)!)
}

answer.sort()

print(answer.last!)