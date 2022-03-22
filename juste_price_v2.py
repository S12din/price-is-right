import random

# WE ADDED CHANCES TO THIS LEVEL
chances = 10
correct_price = random.randint(1, 100)

# WE DECLARED A VARIABLE CALLED GUESSES FOR SAYING IN THE END OF THE GAME TO THE USER IN HOW MANY GUESSES DID HE WIN
guesses = 0

# WHILE CHANCES ARE UPPER THAN 0 THE GAME DOES NOT END IF THERE'S NO EXCEPTION
while chances > 0:
    # WE ASK THE USER TO ENTER A NUMBER BETWEEN 1 AND 100
    ask = input("please enter your number between 1 and 100: ")

    # IF ENTERED NUMBER IS NUMERIC
    if ask.isnumeric():

        # IF ENTERED NUMBER IS BETWEEN 1 AND 100
        if int(ask) < 100 or int(ask) > 0:
            # IF ENTERED NUMBER EQUALS TO THE CORRECT PRICE THE GAME ENDS
            if ask == correct_price:
                # WE INCREASE GUESSES BY 1
                guesses += 1
                print(
                    f"congratulations you have found the number in {chances} chances and the number was {correct_price}")
                break
            # IF ELSE ENTERED NUMBER IS UPPER THAN CORRECT PRICE WE SAY DOWN
            elif ask > correct_price:
                print("go down")
                # WE DECREASE CHANCES BY 1
                chances -= 1
                print(f"You have {chances} chances left")
                # WE INCREASE GUESSES BY 1
                guesses += 1
            # IF ELSE ENTERED NUMBER IS LOWER THAN CORRECT PRICE WE SAY UP
            elif ask < correct_price:
                print("go up")
                # WE DECREASE CHANCES BY 1
                chances -= 1
                print(f"You have {chances} chances left")
                # WE INCREASE GUESSES BY 1
                guesses += 1
        # ELSE WE SAY TO ENTER A NUMBER BETWEEN 1 AND 100
        else:
            print("Enter a number between 1 and 100")
    # IF THE USER DOES NOT ENTER A NUMBER WE ASK HIM TO ENTER A NUMBER NOT A CHARACTER
    else:
        print("enter a number not a character")
# WE TELL TO THE USER IN HOW MANY TRIES DID HE GET THE NUMBER
print("You have got it in ", guesses, "guesses")
