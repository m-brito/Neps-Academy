def eh_primo(x):
    q=0
    for c in range(1, x+1):
        if x%c==0:
            q+=1
    if q==2:
        x=True
        return x
    else:
        x=False
        return x
x = int(input())
if eh_primo(x):
    print('S')
else:
    print('N')
