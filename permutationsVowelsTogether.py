l=input()
vowels=['A', 'E', 'I', 'O', 'U']
vo=0
co=0
i=0
while i<len(l):
    if l[i] in vowels:
        vo+=1
    else:
        co+=1
    i+=1
pro=1
i=1
while i<=len(l):
    pro=pro*i
    i+=1
while vo!=0:
    pro=pro*vo
    vo-=1
print(pro)