#Weekly Study Cost Calculator

#Travel cost per day: £7.50
travel_cost = float(input("Enter your daily travel cost: £"))

#Lunch cost per day: £4.25
lunch_cost = float(input("Enter your daily lunch cost: £"))

#Number of study days: 5
study_days = int(input("Enter your weekly study days: "))

print("----- WEEKLY STUDY COST -----")
print()
#Weekly travel: £37.50
weekly_travel = travel_cost * study_days
print(f"Weekly travel:        £{weekly_travel:.2f}")

#Weekly food: £21.25
weekly_food = lunch_cost * study_days
print(f"Weekly food cost:     £{weekly_food:.2f}")

print("-" * 29)

#Total weekly study cost: £58.75
weekly_cost = weekly_travel + weekly_food
print(f"Total:                £{weekly_cost:.2f}")