x=int(input("enter the number"))
y=int(input("enter the number"))
z=int(input("enter the number"))
if (x>y>z):
    print("second large number is : ",y)
elif (z>y>x):
    print("second large number is :",y)
elif(x>z>y):
    print("second large number is : ",z)
elif(y>z>x):
    print("second large number is : ",z)
elif(y>x>z):
    print("second large number is : ",x)
else:
    print("second large number is : ",x)