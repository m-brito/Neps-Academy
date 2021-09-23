def fatorial(N):
    if N==0:
        N=1
        return N 
    for c in range(N-1, 0, -1):
        N=N*c
    return N
N = int(input())
print(fatorial(N))
