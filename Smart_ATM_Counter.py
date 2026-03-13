correct_pin = 123
attempt = 0 

while True:

    user_input = input("Enter pin :")

    if user_input =="":
        print("Sorry you didn't entered anything")
        continue 

    pin = int(user_input)
    if pin == correct_pin:
        print ("Correct pin")
        break

    else:
        attempt +=1
        print(f"Wrong pin entered, You have {3 - attempt} attempt left")
        if attempt ==3:
            print("Account blocked")
            break