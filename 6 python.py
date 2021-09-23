N=int(input())
V=input().split()
total=0
for i in range(len(V)):
    V[i]=int (V[i])
for a in range(len(V)):
    total=total + V[a]
print(total)
