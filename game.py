# Simple random number guessing game by "The Pulsar (001pulsar)"

# modules section
import os        # for clearing the screen
import sys       # to exit the program
import random    # to guess random number

# game function
def game():
    rangeStart = int(input("Number from: "))
    rangeEnd = int(input("Number to: "))
    chosenNumber = random.randrange(rangeStart, rangeEnd)
    guessedNumber = int(input("Enter your guess: "))

    if (guessedNumber == chosenNumber):
        print(f"Correct guess!\nNumber: {chosenNumber}\nGuess: {guessedNumber}")
        print("\n\nPress enter to go back to main menu..")
        input()
        mainMenu()
    else:
        print(f"Wrong guess!\nNumber: {chosenNumber}\nGuess: {guessedNumber}")
        print("\n\nPress enter to go back to main menu..")
        input()
        mainMenu()

# main menu function
# this function would get called upon executing the program
def mainMenu():
    os.system('clear')
    print("...Number guessing game...")
    print("Enter (1) to start\nEnter (2) to exit")
    mainMenuChoice = int(input())
  # not for dev:
  # update the main menu choice codes so that the choice will be taken automatically upon typing without the need to press enter
  # okie dokie
    
    if (mainMenuChoice == 1):
        game()
    elif (mainMenuChoice == 2):
        sys.exit()
    else:
        print("Invalid choice")
        input()
        mainMenu()
        
mainMenu()
