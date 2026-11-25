#Python
#HTML
#GitHub

skill1 = input("Do you know Python? (yes/no): ")
skill2 = input("Do you know HTML? (yes/no): ")
skill3 = input("Do you know GitHub? (yes/no): ")

print()
print("==============CURRENT SKILLS==============")
print()
print("              Python", skill1)
print("              HTML", skill2)
print("              GitHub", skill3)
print()
print("=" * 40)
print()
print("==========RECOMMENDED NEXT STEP==========")
print()

if skill1 == "yes" and skill2 == "yes" and skill3 == "yes":
    print("You have all the required skills.")
elif skill1 == "yes" and skill2 == "yes" and skill3 == "no":
    print("You know Python and HTML. Practise GitHub.")
elif skill1 == "yes" and skill2 == "no" and skill3 == "no":
    print("You know Python. Practise HTML and GitHub.")
elif skill1 == "no" and skill2 == "no" and skill3 == "yes":
    print("You know GitHub. Practise Python and HTML.")
elif skill1 == "no" and skill2 == "yes" and skill3 == "yes":
    print("You know HTML and GitHub. Practise Python.")
elif skill1 == "no" and skill2 == "yes" and skill3 == "no":
    print("You know HTML. Practise Python and GitHub.")
elif skill1 == "yes" and skill2 == "no" and skill3 == "yes":
    print("You know Python and GitHub. Practise HTML")
else:
    print("Practise Python, HTML and GitHub.")

