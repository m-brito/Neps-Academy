N=int(input())
GOF=str(input())
GC=str(input())
acertos=0
for i in range(N):
    if GC[i]==GOF[i]:
        acertos+=1
print(acertos)
