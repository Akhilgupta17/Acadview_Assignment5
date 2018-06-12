Day=int(input("Enter day:"))
if Day==366:
    print("A Leap Year")
elif Day>366 or Day<365:
        print("Invalid  Entry")
else:
    print("Normal Year")
    
#OR

year=int(input("Enter Year:"))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is A Leap year".format(year))
        else:
            print("{0} is Not a Leap Year".format(year))
    else:
        print("{0} is  a Leap Year".format(year))
else:
    print("{0} is Not a Leap Year".format(year))
            
