num = int(input("please enter the number of the items"))
while(num<=0):
    print("invalid value. Please enter positive values only")
    num = int(input("enter the number of items"))

total = 0.0
for i in range(1,num+1,1):
    price=float(input("enter price for item"))
    print("price=", price)
    total+=price
    print("total here=", total)
if (total>=100.0):
    total=0.9*total
print("the total price of all items purchased is", total)
