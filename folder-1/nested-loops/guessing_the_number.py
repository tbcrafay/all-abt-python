import random

def guessing_game():
    """Plays a guessing game where the user tries to guess a randomly generated number."""

    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    attempts_allowed = 10
    attempts_taken = 0

    print("Welcome to the guessing game!")
    print("I'm thinking of a number between 1 and 100.")

    while attempts_taken < attempts_allowed:
        guess = eval(input("Guess a number: "))
        attempts_taken += 1

        if guess == number:
            print("Congratulations! You guessed the number in", attempts_taken, "attempts!")
            break
        elif guess < number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

        if attempts_taken == attempts_allowed:
            print("Sorry, you ran out of attempts! The number was", number)

# Call the function to start the game
guessing_game()

