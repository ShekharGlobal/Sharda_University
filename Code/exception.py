try:
    amount = float(input("Enter amount: "))
    print(amount)

except ValueError:
    print("Please enter a valid number.")