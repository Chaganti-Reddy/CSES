import sys

n = int(input())
arr = list(map(int, input().split()))
ans = sys.maxsize

def f(i, diff):
    global ans
    if i == n:
        ans = min(ans, abs(diff))
        return
    f(i+1, diff + arr[i])
    f(i+1, diff - arr[i])

f(0, 0)
print(ans)