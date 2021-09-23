def fatorial(N):
    f=N
    while f>1:
        N *=f-1
        f-=1
    return N
N = int(input())
print(fatorial(N))
