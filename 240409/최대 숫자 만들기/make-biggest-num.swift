// 무슨기준으로 sort를 하고 이를 정리하느냐~

// 앞 숫자가 중요하다. 더 짧은 경우에는 뒤에 그 마지막?숫자를 붙여본다
// 18 182 이랑 붙으면
// 18218 > 18182

let N = Int(readLine()!)!

var arr: [Int] = []

for _ in 0..<N {
    let num = Int(readLine()!)!
    arr.append(num)
}

arr.sort {
    var s1 = Array(String($0)).map { Int(String($0))! }
    var s2 = Array(String($1)).map { Int(String($0))! }
    let l1 = min(s1.count, s2.count)
    let l2 = max(s1.count, s2.count)

    s1 = s1 + Array(repeating: s1.last!, count: l2-s1.count)
    s2 = s2 + Array(repeating: s2.last!, count: l2-s2.count)

    // print("s1, s2", s1, s2)

    for i in 0..<l2{ // 모든걸 비교해보기
        if s1[i] == s2[i] {
            continue
        } else {
            return s1[i] > s2[i]
        }
    }
    // 만약 여기까지 왔는데도 안끝난거면 겹치는 부분까지는 똑같음
    
    return true
}

// print(arr)
print(arr.map{ String($0) }.joined(separator: ""))