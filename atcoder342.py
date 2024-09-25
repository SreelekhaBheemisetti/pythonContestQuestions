s=input()
i=0
c=0
cc=1
diff=1
while i<len(s)-1:
    if s[i]!=s[i+1]:
        c+=1
        diff=i+1
    else:
        cc+=1
    i+=1
if c==1 and cc==len(s)-1:
    print(len(s))
elif c==1:
    print(1)
else:
    print(diff)
