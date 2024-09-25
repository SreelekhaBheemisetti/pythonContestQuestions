l=[]
while True:
    n=int(input())
    if n==0:
        l.append(n)
        break
    l.append(n)
for i in range(-1,-len(l)):
    print(l[i])

