water=int(input("enter the number"))
if water<1:
    print("needs to be filled")
elif water>1 and water<10:
    print("no needs to be filled")
else:
    print("overflow")