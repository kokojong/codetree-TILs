n = int(input())

for r in range(n):
    row = []
    for c in range(n):
        row.append(r+1 + c*n)
    print(*row)