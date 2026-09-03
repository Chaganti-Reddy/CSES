import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t_cases = int(data[idx]); idx += 1
    out = []
    for _ in range(t_cases):
        n, a, b = int(data[idx]), int(data[idx+1]), int(data[idx+2])
        idx += 3

        feasible = (a + b <= n) and not ((a == 0) ^ (b == 0))

        if not feasible:
            out.append("NO")
            continue

        out.append("YES")
        t = n - a - b
        m = a + b
        R = list(range(t + 1, n + 1))

        deck1 = list(range(1, n + 1))
        deck2 = list(range(1, t + 1))
        if m > 0:
            deck2.extend(R[(i + a) % m] for i in range(m))

        out.append(' '.join(map(str, deck1)))
        out.append(' '.join(map(str, deck2)))

    sys.stdout.write('\n'.join(out) + '\n')

main()