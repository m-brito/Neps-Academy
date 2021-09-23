e = int(input())
if e>=3 and e<=1000:
    lista=[]
    for a in range(0,e):
        x = list(map(int, input().split()))
        lista.append(x)
    maior=lista[0][0]
    for b in range(0,e):
        for c in range(0,e):
            somaL=0
            somaC=0
            for d in range(e):
                if str(b)+str(c)!=str(b)+str(d):
                    somaL+=lista[b][d]
                if str(b)+str(c)!=str(d)+str(c):
                    somaC+=lista[d][c]
            if somaL+somaC>maior:
                maior=somaL+somaC
    print(maior)
