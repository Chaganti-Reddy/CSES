s = input().strip()
i = 0
ans = 0
n = len(s)
while i < n:
    j = i
    while j < n and s[j] == s[i]:
        j += 1
    ans = max(ans, j - i)
    i = j
print(ans)