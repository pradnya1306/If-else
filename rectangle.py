length1=int(input("enter the 1st length :"))
length2=int (input("enter the 2nd length :"))
breadth1=int(input("enter the 1st breadth : "))
breadth2=int(input("enter the 2nd breadth : "))
if length1==length2==breadth1==breadth2:
    print("square")
elif length1==length2 and breadth1==breadth2:
    print("it is rectangle,not square")
else:
    print("nothing")