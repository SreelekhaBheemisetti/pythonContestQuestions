n=int(input())
l=list(map(int,input().split()))
i=1
pos=l[0]
ans=-1
while i<len(l):
    if l[i]>pos:
        ans=i+1
        break
    i+=1
print(ans)