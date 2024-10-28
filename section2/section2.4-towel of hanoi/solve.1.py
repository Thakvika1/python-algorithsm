def hanoi(n, src, via, dsn) :
    if n == 1 :
        print(f"{src} -> {dsn}")
    else :
        hanoi(n - 1, src, dsn, via)
        hanoi(1, src, via, dsn)
        hanoi(n - 1, via, src, dsn)
N = int(input())
hanoi(N, "A", "B", "C")
print("The time of moves:", (2 ** N)-1)