def f(k):
    return (pow(k, 4) - 9*pow(k, 2) + 24*k - 16) // 2

k = int(input())

for i in range(1, k+1):
    print(f(i))
