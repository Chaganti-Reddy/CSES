n = int(input())
if n == 2 or n == 3:
    print("NO SOLUTION")
elif n == 1:
    print(1)
elif n == 4:
    print(3, 1, 4, 2)
else:
    odds = list(range(1, n+1, 2))
    evens = list(range(2, n+1, 2))
    result = odds + evens
    print(*result)