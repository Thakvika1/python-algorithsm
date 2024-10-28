def insertionsort(n, s) :
    cnt = 0
    for i in range(1, n) : 
        j, val = i - 1, s[i] # so j = 0 and val = s[1]
        cnt += 1
        while j >= 0 and s[j] > val : # if s[0] > s[1]
            s[j + 1] = s[j]  # s[0 + 1] = s[0] switch position 
            j -= 1    # after that j = 0 - 1 so j = -1
            cnt += 1
        s[j + 1] = val     # s[-1 + 1] = val doy val = s[1] switch position
    return cnt

N = int(input())
S = list(map(int, input().split()))
print(insertionsort(N, S))