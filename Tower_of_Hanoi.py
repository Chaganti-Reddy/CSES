import sys

def hanoi(n, src, aux, dst, moves):
    if n == 0:
        return
    hanoi(n - 1, src, dst, aux, moves)   # move n-1 disks src -> aux
    moves.append(f"{src} {dst}")          # move biggest disk src -> dst
    hanoi(n - 1, aux, src, dst, moves)   # move n-1 disks aux -> dst

n = int(input())
moves = []
hanoi(n, 1, 2, 3, moves)
sys.stdout.write(str(len(moves)) + "\n" + "\n".join(moves) + "\n")