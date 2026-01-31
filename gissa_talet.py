# importing random library.

import random

correct_answer = False

counter = 0

highest_score = None

# Choosing a random number in between 1 to 100

real_number = random.randint(1, 100)

# The code repeats until the correct guess is made and writes on the screen how many guesses made.


while correct_answer == False and counter < 10:
    
    counter = counter + 1

    # asking users to guess a number between 1 to 100.

    print('Gissa talet')

    print('Du ska nu gissa ett tal mellan 1 och 100, så varsågod...')

    guess_number = int(input('Skriv in ett tal\n'))

    print(f'Du har gissat {counter} gånger.')

    # the difference between the guessed number and the real number is assigned to a variable

    difference = abs(guess_number - real_number)

    # warning the user if the guessed number is less than 1 or greater than 100

    if guess_number < 1 or guess_number > 100:

        print('Du ska nu gissa ett tal mellan 1 och 100')

    # Notifies user if guess number is lower than the real number and also notifies when user close to the real number.

    elif guess_number < real_number:

        print('Ditt tal är för litet. Gissa på ett större tal')

        if difference <= 3:
            print('Du är dock nära, det bränns')

    # Notifies user if guess number is higher than the real number and also notifies when user close to the real number.

    elif guess_number > real_number:

        print('Ditt tal är för stort. Gissa på ett mindre tal')

        if difference <= 3:
            print('Du är dock nära, det bränns')

    # If guess number equal to real number  program congratulates the user.

    elif guess_number == real_number:

        correct_answer = True

        print('Rätta gissat. Bra jobbat.')

        # If the guessed number is correct, update the highest_score variable with the fastest game time.

        if highest_score is None or counter < highest_score:

            highest_score = counter

        # If guess number equal to real number, program  asks to user if they would like to play again.

        play_again = input('Ska du spela igen? Skriva  ja eller nej\n')

        if play_again == 'ja':
            correct_answer = False

            counter = 0

            real_number = random.randint(1, 100)

    # if user plays the game 10 times, game ends and asks to user, if user would like to play or ends the game.
    if counter == 10:

        play_again = input('Ska du spela igen? Skriva  ja eller nej\n')

        # if user says yes and would like to continue with the game, counter resets and a new real number assigns to the game.
        if play_again == 'ja':
            counter = 0

            real_number = random.randint(1, 100)

    # If no game has been played, the playtime will not be displayed on the screen; otherwise, the record will be shown
if highest_score != None:
    print(f"Du gjorde den snabbaste gissningen på {highest_score} försök.")

print('Programmet Slut.')

	


         
    
    

    

