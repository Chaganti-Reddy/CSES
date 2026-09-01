def spiral(y: int, x: int) -> int:
    m = max(x, y)
    if m % 2 == 1:
        return m*m - y + 1 if x >= y else (m-1)**2 + x
    else:
        return m*m - x + 1 if y >= x else (m-1)**2 + y

t = int(input())
for _ in range(t):
    y, x = map(int, input().split())
    print(spiral(y, x))