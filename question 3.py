#atm transaction simulation
balance = 5000

print("1. Deposit")
print("2. Withdraw")
choice = int(input("Enter your choice: "))
amount = int(input("Enter amount: "))

if choice == 1:
    balance += amount
elif choice == 2:
    if amount <= balance:
        balance -= amount
    else:
        print("Insufficient Balance")
else:
    print("Invalid Choice")

print("Balance: Rs.", balance)