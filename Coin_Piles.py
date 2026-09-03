n = int(input())

def canEmpty(a: int, b: int) -> str:
    if (a + b) % 3 == 0 and max(a, b) <= 2 * min(a, b):
        return "YES"
    return "NO"

while n:
    a, b = map(int, input().split())
    print(canEmpty(a, b))
    n -= 1