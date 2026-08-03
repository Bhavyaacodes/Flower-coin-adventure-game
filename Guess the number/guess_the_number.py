import random
print("Welcome to Guess the Number!")
play = input("Do you want to play? (yes/no): ")
if play.lower() != "yes":
    print("Maybe next time! Goodbye!")
    exit()
else:
    print("Great! Let's start the game.")

secret_number = random.randint(1,100)
x = int(input("Guess the secret number: "))
attempts = 1
while x != secret_number:
    attempts += 1
    if x < secret_number:
        print("Your guess is too low. Try again.")
    else:
        print("Your guess is too high. Try again.")
    x = int(input("Guess the secret number: "))
    print("Congratulations! You've guessed the secret number!")
    print(f"It took you {attempts} attempts to guess the number.")
    print("Thank you for playing Guess the Number!")
    print("Do you want to play again? (yes/no): ")
    play_again = input().lower()
    if play_again == "yes":
        secret_number = random.randint(1,100)
        x = int(input("Guess the secret number: "))
        attempts = 1
    else:
        print("Maybe next time! Goodbye!")
        exit()
