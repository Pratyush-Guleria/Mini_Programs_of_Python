name = input("What is your name :").strip().upper()

college = input("What is your collage name :").strip().upper()

skill = input("Which skill do you have :").strip().upper()

DOB = int(input("In which year you born :").strip())

age = 2026 - DOB

print("-------------------------")
print(f"Student ID: {name}")
print(f"AGE: {age}")
print(f"COLLEGE: {college}")
print(f"SKILL: {skill}")
print("-------------------------")