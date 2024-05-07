monthes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30 ,31, 30, 31]

m1, d1, m2, d2 = map(int, input().split())

accums = [0]
for i in range(1, 13):
    accums.append(accums[i-1] + monthes[i])

b = accums[m2-1] + d2
a = accums[m1-1] + d1

diff = b-a
diff %= 7

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print(days[diff])