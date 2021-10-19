num1=int(input("enter the number"))
num2=int(input("enter the number"))
num3=int(input("enter the number"))
if (num1>num2 and num1<num3) or (num1>num3 and num1<num2):
    print(num1)
elif (num2>num1 and num2<num3) or (num2>num3 and num2<num1):
    print(num2)
else:
    print(num3)
    