# vowel=input("enter the vowel:")
# a=["a","A","e","E","i","I","o","O","u","U"]
# if vowel in a:
#     print("vowel")
# else:
#     print("not vowel")

# a=['1', '2', '3', '4', '5', '6', '7', '8']
# b=[]
# i=0
# while i<len(a)-1:
#     c=a[i]+a[i+1]
#     b.append(c)
#     i+=2
# print(b)

a=[65,98,54,23,87,57]
max1=0
max2=0
max3=0
i=0
while i<len(a):
    if a[i]>max1:
        max1=a[i]
    i+=1
j=0
while j<len(a):
    if a[j]>max2 and a[j]!=max1:
        max2=a[j]
    j+=1
k=0
while k<len(a):
    if a[k]>max3 and a[k]!=max2 and a[k]!=max1:
        max3=a[k]
    k+=1
print(max1)
print(max2)
print(max3)