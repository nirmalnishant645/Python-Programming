def DBill(units):
    if (units < 200):
        price = units*1.20
    elif (200<=units<400):
        price = units*1.50
    elif (400<=units<600):
        price = units*1.80
    elif (units>=600):
        price = units*2.00
    else:
        print("Invalid Input")
    if (price <= 100):
        price = 100
        print(price)
    elif (price>400):
        price+=15*price/100
        print(price)
    else:
        print(price)

def IBill(units):
    price = units*6.00
    print(price)

type = str(input("Enter 'D' for Domestic Meter and 'I' for Industrial Meter: "))
cr = int(input("Enter Current Reading of meter: "))
pr = int(input("Enter Previous Reading of meter: "))
units = cr-pr

if (type == 'D' or type == 'd'):
    DBill(units)
elif (type == 'I' or type == 'i'):
    IBill(units)
else:
    print("Invalid Meter Type")
