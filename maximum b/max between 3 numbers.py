a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
if a>b and a>c:
    print("a is max:",a)
elif b>a and b>c:
    print("b is max:",b)
else:
    print("c is max:",c)