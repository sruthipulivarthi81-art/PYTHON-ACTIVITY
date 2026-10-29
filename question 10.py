#water tank level calculator
capacity = int(input("Enter tank capacity in litres: "))
water = int(input("Enter current water level: "))
used = int(input("Enter water used: "))

remaining = water - used

if remaining < 0:
    print("Not enough water")
else:
    print("Remaining Water:", remaining, "litres")