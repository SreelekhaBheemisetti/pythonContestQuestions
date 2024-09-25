s=input()
s1=s[0]
s2=s[1:]
if len(s)==1 and s1.isupper():
    print("Yes")
elif s1.isupper() and s2.islower():
    print("Yes")
else:
    print("No")