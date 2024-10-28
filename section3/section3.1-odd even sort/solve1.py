def solve(n) :
    listeven = []
    listodd = []
    for i in range(1, n + 1) :
        if n % 2 == 0 :
            listeven.append(i)
        else :
            listodd.append(i)
    return listeven

N = int(input())
print(solve(N))
