#Collect information

#Name
name = input("What is your name? ")

#Career goal
career_goal = input("What is your career goal? ")

#Programming language they are learning
programming_language = input("What programming language are you learning? ")
learning_python = True

#Hours they study per day
study_hours = float(input("What are the daily study hours? "))

#Days they study per week
study_days = int(input("What are the weekly study days? "))

#Favourite way to learn
favourite_learning_method = input("What is your favourite way to learn? ")

weekly_study_hours = study_hours * study_days
print()
print("========== MY LEARNING PROFILE ==========")
print()

print("Name:",                     name)
print("Career goal:",               career_goal)
print("Learning Python:",           learning_python)
print(f"Study hours:               {study_hours:.2f} hours/day")
print(f"Study days:                {study_days} days/week")
print("Favourite way to learn:",    favourite_learning_method)
print("-" * 40)
print(f"Weekly study hours:        {weekly_study_hours:.2f} hours/week")
print()
print("=" * 40)

