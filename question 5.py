#mobile plan cost calculator
usage = int(input("Enter data usage in GB: "))

if usage <= 2:
    cost = 100
elif usage <= 5:
    cost = 200
else:
    cost = 300

print("Mobile Plan Cost: Rs.", cost)