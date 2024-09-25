# n=int(input())
# str1="L"
# str2="ng"
# i=0
# while i<n:
#     str1+="o"
#     i+=1
# print(str1+str2)

# import math
# n=int(input())
# n=bin(n)[2:]
# i=0
# c=0
# while i<len(n):
#     if n[i]=="0":
#         c+=1
#     else:
#         c=0
#     i+=1
# print(c)

# n=int(input())
# c=0
# i=1
# while i<=n:
#     # j=1
#     dig_sum=0
#     while i!=0:
#         dig=i%10
#         dig_sum=dig_sum+dig
#         i=i//10
#     if i%dig_sum==0:
#         c+=1
#     i+=1
# print(c)

# if "b"<"a":
#     print("b")
# else:
#     print("a")


# for n in range(int(input())):
#     sx=0
#     sy=0
#     x,y=map(int,input().split())
#     sx=sx+x
#     sy=sy+y
# if sx>sy:
#     print("Takahashi")
# elif sx<sy:
#     print("Aoki")
# else:
#     print("Draw")

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

    
