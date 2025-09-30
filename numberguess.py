""" 
Author:Ken Lambert
Plays a game of guess the number with the user. 
"""

import random
def main ():
    """ Inputs the bounds of the range of numbers and lets the user guess the computer's number
    until the guess is correct."""
    smaller_nbs = int (input("Enter the smaller number: "))
    larger_nbs = int (input("Enter the larger number: "))
    myNumber_nbs = random.randint (smaller_nbs, larger_nbs)
    count = 0
    while True:
        count +=1
        userNumber_nbs=int(input("Enter your guess: "))
        if userNumber_nbs<myNumber_nbs:
            print("Too small")
        elif userNumber_nbs>myNumber_nbs:
            print("Too larger_nbs")
        else:
            print("You've got it in", count, "tries!")
            break

if __name__ == "__main__":
    main()

