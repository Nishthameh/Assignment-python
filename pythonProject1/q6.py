a=int(input("enter first side"))
b=int(input("enter second side"))
c=int(input("enter third side"))
if c>a+b or a>b+c or b>a+c:
    print("no")
elif a==0 or b==0 or c==0:
    print("length cant be zero")
else:
    print("yes")

