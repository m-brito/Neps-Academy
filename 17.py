i = int(input())
if i>=2 and i<=10:
    l=[]
    somas=[]
    for a in range(0,i):
        n=list(map(int,input().split()))
        l.append(n)
    somaD=0
    somaD2=0
    for b in range(0, i):
        somaD+=l[b][b]
        somaD2+=l[b][i-b-1]
        somaL=0
        somaCO=0
        for c in range(0, i):
            somaL+=l[b][c]
            somaCO+=l[c][b]
        somas.append(somaL)
        somas.append(somaCO)
    somas.append(somaD)
    somas.append(somaD2)
    resp=0
    for g in range(0,len(somas)):
        if somas[0]!=somas[g]:
            resp=-1
    if resp==0:
        print(somas[0])
    else:
        print(-1)
