month=input("enter the month")
if month=="january":
    print("31")
elif month=="february":
    print("28 or 29")
elif month=="march":
    print("31")
elif month=="april":
    print("30")
elif month=="may":
    print("31")
elif month=="june":
    print("30")
elif month=="jully":
    print("31")
elif month=="auguest":
    print("31")
elif month=="september":
    print("30")
elif month=="october":
    print("31")
elif month=="november":
    print("30")
elif month=="december":
    print("31")
else:
    print("we have only twelve months of the year")

year=input("enter the year")
if year in ("january","march","may","jully","august","october","december"):
    print("31")
elif year in ("april","june","september","november"):
    print("30")
elif year=="february":
    print("28")