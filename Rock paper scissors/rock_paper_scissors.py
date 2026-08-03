print("Welcome to rock-paper-scissors!") 
x = input("Do you want to play? (yes/no): ") 
your_points = 0 
my_points = 0 
if x.lower() != "yes": 
    print("Maybe next time! Goodbye!") 
else: 
    print("Great! Lets start the game!") 
    print("Choose your move: rock, paper or scissors") 
    import random 
    choices = ["rock", "paper", "scissors"] 
    while your_points < 5 and my_points < 5: 
        user_input = input().lower() 
        print(f"you chose {user_input}") 
        if user_input not in choices: 
            print("Invalid choice. Please choose rock, paper or scissors.") 
            continue 
        my_choice = random.choice(choices) 
        print(f"I chose: {my_choice}") 
        if user_input == my_choice: 
            print("It's a tie!") 
            
        elif (user_input == "rock" and my_choice == "scissors") or (user_input == "paper" and my_choice == "rock") or (user_input == "scissors" and my_choice == "paper"): 
            print("You win this round!") 
            your_points += 1 
        else: 
            print("You lose this round!") 
            my_points += 1 
        print(f"You: {your_points}, Me: {my_points}") 
        print("Next round!")
        print("Choose your move: rock, paper or scissors")
        if your_points == 5: 
         print("Congratulations! You won the game!") 
        elif my_points == 5: 
         print("I won the game! Better luck next time!")