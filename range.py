down = 0
up = 100
for i in range (1,10):
    guessend_age = int((up + down)/2)
    answer = input("are you"+str(guessend_age)+"year old? ")
    if answer == "correct":
        print("Nice")
        break
    elif answer == 'less':
        up = guessend_age
    elif answer == "more":
        down = guessend_age
    else:
        print("wrong answer")

