qtd = int(input())
if qtd>=1 and qtd<=100:
    bandeijas = []
    quebrados=0
    for i in range(0,qtd):
        lista = []
        L,C = input().split(" ")
        L=int(L)
        C=int(C) 
        while L<0 or L>100 or C<0 or C>100:
            L,C = input().split(" ")
            L=int(L)
            C=int(C) 
        lista.append(L)
        lista.append(C)
        bandeijas.append(lista)
        
    for a in bandeijas:
        if a[0]>a[1]:
            quebrados+=a[1]
    print(quebrados)
    
