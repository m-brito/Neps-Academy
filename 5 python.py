A, B, C=input().split()
ganhador=None
if A != B and A !=C:
    ganhador="A"
elif B != A and B != C:
    ganhador="B"
elif C !=A and C !=B:
    ganhador="C"
else:
    ganhador="*"
print(ganhador)
