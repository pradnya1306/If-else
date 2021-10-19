currentyear=int(input("enter the current year"))
birthyear=int(input("enter the birth year"))
futureyear=int(input("enter the future year"))
current_age=0
future_age=0
if currentyear>1:
    current_age=currentyear-birthyear
    print("current age=",current_age)
if birthyear>1:
    future_age=futureyear-birthyear
    print("future age=",future_age)
else:
    print("invalid year")