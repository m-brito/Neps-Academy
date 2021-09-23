qtd=int(input())
if qtd>=2 or qtd<=10**5:
    Lista = input().split(" ")
    A=0
    B=0
    for a in range(0,qtd):
        var=int(Lista[a])
        if var==1:
            if A==1:
                A=0
            else:
                A=1
        if var==2:
            if A==1:
                A=0
            if A==0:
                B=1
            if B==1:
                A=0
            if B==0:
                B=1
    print(A)
    print(B)
