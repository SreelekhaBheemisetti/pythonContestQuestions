# a,b=map(int,input().split())
# if (a==b):
#     print(-1)
# elif (a==1 or a==2) and (b==2 or b==1):
#     print(3)
# elif (a==2 or a==3) and (b==3 or b==2):
#     print(1)
# else:
#     print(2)


n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort()
b.sort()
j=0
flam=True
while j<n:
    if a[j] in b:
        flam=False
        break
    j+=1
if flam==True:
    flag=False
    i=0
    while i<n-1:
        if a[i]-a[i+1]==-1:
            flag= True
            break
        i+=1
    c=a+b
    c.sort()
    if flag==True:
        print("Yes")
    else:
        print("No")
else:
    print("No")
