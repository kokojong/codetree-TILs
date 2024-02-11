def print_rect(n, m):
    for _ in range(0, n):
        print("1" * m)

row_num, col_num = tuple(map(int, input().split()))
print_rect(row_num, col_num)