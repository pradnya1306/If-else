
sex=input("enter the sex")
age= int(input("enter the age"))
marital_status=input("enter the status")
if sex=='female':
    print("work only in urban areas")
elif sex== 'male' and (age>=20 and age<=40):
    print("work in anywhere")
elif sex=='male' and (age>=40 and age<=60):
    print("only work in urban area")
else:
    print(" error")