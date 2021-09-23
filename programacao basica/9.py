a,b= input().split(" ")
a = float(a)
b = float(b)
m = (a+b)/2
if m>=7:
    print("Aprovado")
elif m>=4:
    print("Recuperacao")
else:
    print("Reprovado")
