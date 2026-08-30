n = int(input())

while n != 1:
    print(n, end=' ', flush=True)
    if n % 2 != 0:
        n = n*3 + 1
    else:
        n = n // 2

print(n)
