s=input()
dic={}
s=list(s)
i=0
while i<len(s):
    dic[s[i]]=s.count(s[i])
    i+=1
print(dic)
# flag=True
# j=0
# while j<len(dic):
#     k=j+1
#     while k<len(dic):
#         if dic[j]==