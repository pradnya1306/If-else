# x=int(input("enter the number"))
# if x%10!=0:
#     x=x//10
#     if x%10!=0:
#         x=x//10
#         if x%10!=0:
#             x=x//10
#             if x%10!=0:
#                 x=x//10
#             else:
#                 print("nothing")
#         else:
#             print("nothing")
#     else:
#         print("nothing")
# else:
#     print("nothing")

a=int(input("enter the number"))
n=a%10
a=a//10
n1=a%10
a=a//10
b=(n*100)+(n1*10)+a
if b>100:
    print(b,"is reverse number")
else:
    print(b"not reverse number")