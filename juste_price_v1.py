from random import randint

correct_price = randint(1,100)

progress=True
while progress:
    ask=int(input("Enter a number between 1 and 100 : "))

    if ask == correct_price:
        print("Congratulations you find the number")
        progress = False
    elif ask > correct_price:
        print("go down")
    elif ask < correct_price:
        print("go up")
    else:
        print("You have to put a number between 1 and 100")