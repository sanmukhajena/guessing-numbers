import random
def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    while True:
        try:
            x = int(input("Enter the lower bound (X): "))
            y = int(input("Enter the upper bound (Y): "))
            if x >= y:
                print("The lower bound must be less than the upper bound. Please try again.")
            else:
                break
        except ValueError:
            print("Please enter valid integers for the bounds.")
    secret_number = random.randint(x, y)
    guesses = 0
    print(f"Guess the number between {x} and {y}.")
    while True:
        try:
            guess = int(input("Enter your guess: "))
            guesses += 1
            if guess < x or guess > y:
               print(f"Your guess must be between {x} and {y}.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {guesses} guesses.")
                break
        except ValueError:
            print("Please enter a valid integer for your guess.")
number_guessing_game()
