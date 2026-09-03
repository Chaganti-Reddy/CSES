from collections import Counter

s = input()
counts = Counter(s)
odd_chars = [c for c, n in counts.items() if n % 2]

if len(odd_chars) > 1:
    print("NO SOLUTION")
else:
    half = ''.join(c * (n // 2) for c, n in counts.items())
    middle = odd_chars[0] if odd_chars else ''
    print(half + middle + half[::-1])