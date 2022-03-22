import random

# WE DECLARE A VARIABLE CALLED CORRECT_PRICE WITH RANDOM
correct_price = random.randint(1, 100)

# WE DECLARE A VARIABLE CALLED PROGRESS WITH A BOOLEAN VALUE TO NOT USE BREAK IN WHILE LOOP
progress = True
while progress:
    # WE ASK THE USER TO ENTER A NUMBER BETWEEN 1 AND 100
    ask = input("Enter a number between 1 and 100 : ")

    # IF ENTERED NUMBER IS NUMERIC
    if ask.isnumeric():
        # IF ENTERED NUMBER IS BETWEEN 1 AND 100
        if int(ask) < 100 or int(ask) > 0:
            # IF ENTERED NUMBER EQUALS TO THE CORRECT PRICE THE GAME ENDS
            if int(ask) == correct_price:
                print("Congratulations you find the number", correct_price)
                progress = False
            # IF ELSE ENTERED NUMBER IS UPPER THAN CORRECT PRICE WE SAY DOWN
            elif int(ask) > correct_price:
                print("go down")
            # IF ELSE ENTERED NUMBER IS LOWER THAN CORRECT PRICE WE SAY UP
            elif int(ask) < correct_price:
                print("go up")
        # ELSE WE SAY TO ENTER A NUMBER BETWEEN 1 AND 100
        else:
            print("Enter a number between 1 and 100")
    # IF THE USER DOES NOT ENTER A NUMBER WE ASK HIM TO ENTER A NUMBER NOT A CHARACTER
    else:
        print("enter a number not a character")
