Quantity=int(input("Enter Quantity :"))
if Quantity*100>1000:
    cost=Quantity*100
    print("total cost : %d" % cost)
    print("You Get 10% Discount")
    finalcost=(cost-(cost*10/100))
    print("After discount You Pay: %d" % finalcost)
else:
    print("You Will Not Get Any Discount")
