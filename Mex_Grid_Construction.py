n = int(input())

grid = [[0] * n for _ in range(n)]
col_used = [set() for _ in range(n)]

for i in range(n):
    row_used = set()
    for j in range(n):
        v = 0
        while v in row_used or v in col_used[j]:
            v += 1
        grid[i][j] = v
        row_used.add(v)
        col_used[j].add(v)

for row in grid:
    print(' '.join(map(str, row)))