import sys

def place(row):
    global answer
    if row == n:
        answer += 1
        return
    for col in range(n):
        if grid[row][col] == '*':
            continue
        if col_attacked[col]:
            continue
        if diag1_attacked[row + col]:
            continue
        if diag2_attacked[row - col + n - 1]:
            continue

        col_attacked[col] = True
        diag1_attacked[row + col] = True
        diag2_attacked[row - col + n - 1] = True

        place(row + 1)

        col_attacked[col] = False
        diag1_attacked[row + col] = False
        diag2_attacked[row - col + n - 1] = False

def main():
    global n, grid, col_attacked, diag1_attacked, diag2_attacked, answer
    n = 8
    grid = [input() for _ in range(n)]
    col_attacked = [False] * n
    diag1_attacked = [False] * (2 * n - 1)
    diag2_attacked = [False] * (2 * n - 1)
    answer = 0

    sys.setrecursionlimit(10000)
    place(0)
    print(answer)

if __name__ == "__main__":
    main()
