basic_salry=int(input("enter the salary"))
if basic_salry<=10000:
    HRA=basic_salry*20/100
    DA=basic_salry*80/100
    print("gross salary=",basic_salry+HRA+DA)

elif basic_salry<=20000:
    HRA=basic_salry*25/100
    DA=basic_salry*90/100
    print("gross salary=",basic_salry+HRA+DA)

else :
    HRA=basic_salry*30/100
    DA=basic_salry*95/100
    print("gross salary=",basic_salry+HRA+DA)