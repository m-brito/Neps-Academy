x,y=input().split()
x=float(x)
y=float(y)
if x>=0 and x<=10000 and y>=1 and y<=10:
    calc=x**y
    if calc<=10**9:
        print('{:.4f}'.format(calc))
