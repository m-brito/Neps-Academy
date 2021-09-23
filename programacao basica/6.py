p1, c1, p2, c2 = input().split(" ")
p1 = int(p1)
c1 = int(c1)
p2 = int(p2)
c2 = int(c2)
while p1<10 or p1>100 or c1<10 or c1>100 or p2<10 or p2>100 or c2<10 or c2>100:
    p1, c1, p2, c2 = input().split(" ")
    p1 = int(p1)
    c1 = int(c1)
    p2 = int(p2)
    c2 = int(c2)
if p1*c1==p2*c2:
    print("0")
elif p1*c1>p2*c2:
    print("-1")
else:
    print("1")
