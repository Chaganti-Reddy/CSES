t = int(input())
n = list(map(int, input().split()))

ans = 0
m = n[0]
for i in range(1, t):
    if n[i] < m:
        ans += m - n[i]
    m = max(m, n[i])

print(ans)