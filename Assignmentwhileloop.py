secret_number = 7
past_guesses = []
guess = 0 

while guess != secret_number:
    
    guess = int(input("Guess the secret number (1-10): "))
    
    past_guesses.append(guess)

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("CORRECT! You win!")

