#railway ticket fare calculator
distance = int(input("Enter distance in km: "))

if distance <= 100:
    fare = distance * 2
elif distance <= 300:
    fare = distance * 3
else:
    fare = distance * 4

print("Railway Fare: Rs.", fare)