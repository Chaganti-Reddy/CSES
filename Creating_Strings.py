def solve():
    s = sorted(input().strip())
    n = len(s)
    used = [False] * n
    temp = []
    results = []

    def backtrack():
        if len(temp) == n:
            results.append("".join(temp))
            return
        for i in range(n):
            if used[i]:
                continue
            if i > 0 and s[i] == s[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            temp.append(s[i])
            backtrack()
            temp.pop()
            used[i] = False

    backtrack()
    print(len(results))
    print("\n".join(results))

solve()