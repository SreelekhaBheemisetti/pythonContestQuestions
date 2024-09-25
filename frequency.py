s=input()
dic={}
for i in range(len(s)):
    dic[s[i]] = s.count(s[i])
max=0
max_t='a'
txt='a'
txt_c=0
for i,j in dic.items():
    if i<txt:
        txt=i
        txt_c=j
    if j>=max:
        max=j
        max_t=i
if max==txt_c:
    print(txt)
elif max>1:
    print(max_t)
else:
    print(txt)
