X=int(input())
if X<=10**4:
    Divs=[]
    for a in range(1,X+1):
        if X%a==0:
            Divs.append(a)
    resp=""
    for a in Divs:
        resp+=str(a)+" "
    print(resp[0:len(resp)-1])
