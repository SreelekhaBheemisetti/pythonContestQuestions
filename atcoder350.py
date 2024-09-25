# s=input()
# ss=s[0:3]
# sl=s[3:]
# sl=int(sl)
# if ss=="ABC" and (sl>000 and sl<=315) or (sl>=317 and sl<=349):
#     print("Yes")
# else:
#     print("No")

n,q=map(int,input().split())
t=list(map(int,input().split()))
l=[]
i=1
while i<=n:
    l.append(i)
    i+=1
j=0
while j<len(t):
    if t[j] in l:
        ind=l.index(t[j])
        l[ind]=0
    elif t[j] not in l:
        ind=l.index(0)
        l[ind]=t[j]
    j+=1
c=0
k=0
while k<len(l):
    if l[k]!=0:
        c+=1
    k+=1
print(c)
