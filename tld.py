s=input()
n=len(s)
i=n-1
ans=""
while i>=0:
    if s[i]!=".":
        ans=s[i]+ans
    else:
        break
    i-=1
print(ans)

# atcoder.jp
# translate.google.com
# .z
# ..........txt
