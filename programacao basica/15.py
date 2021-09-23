N=int(input())
if N>=1 and N<=10000:
    L=input().split()
    for a in range(0,N):
        num=float(L[a])
        if num>=0 and num<=10**9: 
            print('{:.4f}'.format(num**(1/2)))
