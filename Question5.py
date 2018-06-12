Quantity=int(input("Enter Quantity :"))
cost=Quantity*100
if cost>1000:
    print("total cost : %d" % cost)
    print("You Get 10% Discount")
    finalcost=(cost-(cost*10/100))
    print("After discount You Pay: %d" % finalcost)
else:
    print("You Will Not Get Any Discount")
    print("You Have to PAY : %d" %cost)
