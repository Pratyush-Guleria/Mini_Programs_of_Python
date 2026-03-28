while True :

    name = input("What's your name :").strip().capitalize()

    if name =="":
        print("You didn't enter your name")
    else:
        print(f"Hey : {name}")
        break

while True :

    age_input = input(f"Hey : {name}, What's your age :").strip()

    try:
        age = int(age_input)

        if age < 0:
            print(f"Sorry :{name}, You are not born yet")

        elif age < 18:
            print(f"Hey :{name}, Your are a minor")
            break


        else:
            print(f"Hey :{name}, You are an adult ")
            break

    except ValueError:
        print("Plz enter integers only")
