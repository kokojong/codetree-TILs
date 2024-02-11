input_num1, input_num2 = map(int, input().split())

#최대공약수
def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)
    
print(gcd(input_num1, input_num2))