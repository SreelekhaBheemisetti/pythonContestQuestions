s=input()
if len(s)==1:
    print("Yes")
else:
    flag=True
    for i in range(len(s)):
        if s[i]>=s[i+1]:
            flag=False
    if flag==True:
        print("Yes")
    else:
        print("No")

    
