qtd=int(input())
if qtd>=0 and qtd<=1000:
    lista=[]
    for a in range(0,qtd):
        A=int(input())
        while A<0 or A>10**6:
            A=int(input())
        lista.append(A)
    acessos=0
    dias=0
    for a in lista:
        acessos+=a
        
        print(a, acessos)
        if acessos+a<10**6:
            dias+=1
    print(dias+1)
        
    
