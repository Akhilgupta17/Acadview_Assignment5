points=int(input("Enter Points:"))
if points<=50: 
    print("You Won No Prize")
elif points>50 and points<=150:
    print("You won Wooden dog")
elif points>150 and points<=180:
    print("You Won Book")
elif points>180 and points<=200:
    print("You Wion chocolates")
else:
    print("You Won Nothing")
