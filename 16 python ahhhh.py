N = int(input())
E = [int(x) for x in input().split(' ')]
E.sort()
for i in range(N):
    if i < N-1:
        print(E[i], end=' ')
    else:
        print(E[i])
