#Debt Calculator

principal = float(input("Enter your principal amount:£ "))
interest_rate = float(input("Enter your interest rate per year:% ")) / 100
time = float(input("Enter the time you have to pay it back, in years: "))

interest = principal * interest_rate * time
total_amount = principal + interest
print("The total amount to be paid back is: ", total_amount)

if total_amount >= 2000 and total_amount <= 4999:
    print("You have a moderate debt.")
elif total_amount >= 5000 and total_amount <= 8000:
    print("You have a high debt.")
elif total_amount > 8000:
    print("You have a very high debt.")
else:
    print("You have a very low debt.")