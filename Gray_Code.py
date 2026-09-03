n = int(input())

def gray_code(n):
    return [format(i ^ (i >> 1), f'0{n}b') for i in range(1 << n)]

codes = gray_code(n)
for i in range(len(codes)):
    print(codes[i])