import random



while True:
    level=int(input("do you want to play level one or level two (1 or 2) "))
        
    if level==1:
        correct_price = random.randint(1,100)

        progress=True
        while progress:
            ask=int(input("Enter a number between 1 and 100 : "))

            if ask == correct_price:
                print("Congratulations you found the number")
                progress = False
            elif ask > correct_price:
                print("go down")
            elif ask < correct_price:
                print("go up")
            else:
                print("You have to put a number between 1 and 100")
        break
    elif level == 2:
        chances = 10
        correct_price = random.randint(1, 100)

        tries=0
       
        while chances > 0:
            
            ask= int(input("please enter your number between 1 and 100: "))
            if ask == correct_price:
                tries+=1
                print(f"congratulations you have found the number in {tries} tries")
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
        break
    else:
        print("enter 1 or 2 to choose a level")