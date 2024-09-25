# a,b,d=map(int,input().split())
# i=a
# while i<=b:
#     print(i)
#     i+=d
a=[]
for t in range(int(input())):
    
    x,q=map(int,input().split())
    
    if x==1:
        a.append(q)
    else:
        b=-q
        print(a[b])