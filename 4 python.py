A, B=input().split()
A=float(A)
B=float(B)
media=(A+B)/2
Resposta=""
if media >= 7:
    Resposta="Aprovado"
elif media >=4:
    Resposta="Recuperacao"
else:
    Resposta="Reprovado"
print(Resposta)
