monthes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30 ,31, 30, 31]

m1, d1, m2, d2 = map(int, input().split())
target = input()

accums = [0]
for i in range(1, 13):
    accums.append(accums[i-1] + monthes[i])

b = accums[m2-1] + d2
a = accums[m1-1] + d1

diff = b-a
M = diff//7
N = diff%7
# print(a, b)
# print("diff", diff, M, N)
# 5 37 diff 32 -> 5일이 월요일

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
idx1 = days.index(target)

# last = days[N] # 최종 요일
idx2 = N

answer = 0
answer += M
if N >= idx1:
    answer += 1

print(answer)