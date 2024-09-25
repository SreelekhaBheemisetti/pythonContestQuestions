x,y=map(int,input().split())
total=x//y
ans=total+(x-total)
if x<y:
    print(x)
else:
    print(ans)