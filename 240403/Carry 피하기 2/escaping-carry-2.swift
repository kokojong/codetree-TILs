// 각각의 자릿수를 모두 더해봤을 때 10이상 되는 경우가 없도록

// 20개중에 3개 뽑기

let N = Int(readLine()!)!

var arr: [Int] = []

for _ in 0..<N {
    arr.append(Int(readLine()!)!)
}

func check(a:Int, b: Int, c: Int) -> Bool {
    var a = Array(String(a))
    var b = Array(String(b))
    var c = Array(String(c))

    let l = max(a.count, b.count, c.count)
    a = Array(repeating: "0", count: l - a.count) + a
    b = Array(repeating: "0", count: l - b.count) + b
    c = Array(repeating: "0", count: l - c.count) + c

    for i in 0..<l {
        // print( Int(String(a[i])!, Int(b[i])!, Int(c[i])! )
        if (Int(String(a[i]))! + Int(String(b[i]))! + Int(String(c[i]))!) > 9 {
            return false
        }
    }
    
    return true
}

var answer: [Int] = []

for i in 0..<N {
    for j in 0..<i {
        for k in 0..<j {
            let a = Int(String(arr[i]))!
            let b = Int(String(arr[j]))!
            let c = Int(String(arr[k]))!
            // print(a, b, c)
            if check(a: a, b: b, c: c) {
                // print("a, b, c", a, b, c)
                answer.append(a + b + c)
            }
        }
    }
}

answer.sort()
print(answer.last ?? -1)