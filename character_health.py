#Game character

name = input("Enter your character's name: ")
health = int(input("Enter your character's health: "))

if health >= 80 and health <= 100:
    print(name, "is in great shape!")
elif health >= 60 and health <= 79:
    print(name, "is in good shape.")
elif health >= 40 and health <= 59:
    print(name, "is in bad shape.")
elif health >= 1 and health <= 39:
    print(name, "is in critical condition!")
elif health == 0:
    print(name, "is dead.")
else:
    print("Invalid health value. Please enter a value between 0 and 100.")


