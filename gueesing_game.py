
#This is a program where the user gets to guess the Jackpot number within 5 chances
#If he guesses it in more than 5 chances then he looses


num=18
guess = int(input("Guess the number to win the Jackpot\n"))
print("Remember that you have only 5 chances")
i=1
while i <=5:
    if guess < num:
        guess = int(input("Jackpot number is greater please enter again \n"))
    elif guess > num:
        guess = int(input("Jackpot number is smaller please enter again\n"))
    else:
        print("Hurray!! you won the jackpot")
    i=i+1

if i<=5:
    print("You took"+" "+i+"chances")
else:
    print("Sorry!! you took more than 5 chances to guess:(")
