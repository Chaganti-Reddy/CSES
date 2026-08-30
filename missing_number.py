n = int(input())
nums = map(int, input().split())
print((n * (n + 1) // 2) - sum(nums))
