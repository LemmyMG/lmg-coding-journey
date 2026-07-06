secret_number = 4

guess_number = 0

while guess_number != secret_number:
    guess_number = int(input("Guess a number between 1 and 10: "))

    if guess_number < secret_number:
        print("Too low! Try again.")
    elif guess_number > secret_number:
        print("Number too high!")
    else:
        print("Congratulations! You guessed the correct number.")