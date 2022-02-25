import random

chances = 10
correct_price = random.randint(1, 100)

tries=0
guesses=0
while chances > 0:
    guesses += 1
    ask= int(input("Please enter your number between 1 and 100: "))
    if ask == correct_price:
        tries+=1
        print(f"Congratulations you have found the number in {tries}")
        break
    elif ask > correct_price:
        print("go down")
        chances -= 1
        tries +=1
    elif ask < correct_price:
        print("go up")
        chances -=1
        tries +=1
    else:
        print("enter a number between 1 and 100")
print("You have got it in ", guesses, "guesses")