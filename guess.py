""""
The program will first randomly generate a number unknown to the user.
The user needs to guess what that number is.
(In other words, the user needs to be able to input information.)
If the user’s guess is wrong, the program should return some sort of indication as to how wrong
(e.g. The number is too high or too low). If the user guesses correctly, a positive indication should appear.
 You’ll need functions to check if the user input is an actual number, to see the difference between the
 inputted number and the randomly generated numbers, and to then compare the numbers.

"""

import random
generated_number= random.randint(1,100)
print(generated_number)

guessed=True
def num_comparison(guess1,generated):
    guess=guess1
    generated_number=generated
    if guess==generated_number:
        print("Success")
    elif guess>generated_number:
        print("Too high")
    elif guess<generated_number:
        print("Low")
while guessed==True:
    guess = int(input('Input guessed number'))
    guessed=False
    generated_number = random.random()
    num_comparison(guess,generated_number)
