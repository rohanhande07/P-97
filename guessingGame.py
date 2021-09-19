import random

value = random.randint(1,9)
print(value)
guess = int(input("Guess a number between 1 and 9 "))
chances = 5
while chances <= 5:
    if(guess < value):
        print("Your guess is too low")
        guess = int(input("Guess the number"))
    elif(guess > value):
        print("Your guess is too high")
        guess = int(input("Guess the number"))
    if(guess == value):
        print("Congrajulations: you won!")
        break
    chances = chances - 1

    if(chances == 0):
        print("You lose! The number was ", value)
        break