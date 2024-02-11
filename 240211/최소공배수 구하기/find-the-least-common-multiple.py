input_num1, input_num2 = map(int, input().split())

def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)

def lcm(n, m):
    return n * m / gcd(n, m)

print(int(lcm(input_num1, input_num2)))