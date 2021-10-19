num=int(input("enter the number"))
if num>=0:
    print(-num)
elif num==0:
    print(0)
else:
    print(-(num))

a=[5,6,7,8,3,2,1,5]
i=0
while i<len(a):
    a.pop(i)
    i=i+1
print(a)