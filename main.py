import random

computer_score = 0
your_score = 0

while True:

    while True:
        user_choice = input("Enter a choice (rock, paper, scissor): ")
        if user_choice.lower() not in ["rock", "paper", "scissor"]:
            print("Invalid input, it's either a rock or paper or scissor.")
            continue
        else:
            break

    possible_choices = ["rock", "paper", "scissor"]
    computer_choice = random.choice(possible_choices)

    print(
        f"Your choice: {user_choice}. \nComputer choice: {computer_choice}.\n")

    if user_choice == computer_choice:
        print("It's a tie.")
    elif user_choice == "rock":
        if computer_choice == "scissor":
            your_score += 1
            print(
                f"Rock smashes scissor! You win.\nYour score: {your_score} points\nComputer score: {computer_score} points")
        else:
            computer_score += 1
            print(
                f"Paper covers rock! Computer win.\nYour score: {your_score} points\nComputer score: {computer_score} points")
    elif user_choice == "paper":
        if computer_choice == "rock":
            your_score += 1
            print(
                f"Paper covers rock! You win. \nYour score: {your_score} points\nComputer score: {computer_score} points")
        else:
            computer_score += 1
            print(
                f"Scissor cuts paper! Computer win. \nYour score: {your_score} points\nComputer score: {computer_score} points")

    elif user_choice == "scissor":
        if computer_choice == "paper":
            your_score += 1
            print(
                f"Scissor cuts paper! You win. \nYour score: {your_score} points\nComputer score: {computer_score} points")
        else:
            computer_score += 1
            print(
                f"Rock smashes scissor! computer win. \nYour score: {your_score} points\nComputer score: {computer_score} points")

    while True:
        play_again = input("Play again? (Y/N): ")
        if play_again.lower() not in ["y", "n"]:
            print("Invalid input, it's either Y for playing again or N for stop playing.")
            continue
        else:
            break
    if play_again.lower() != "y":
        break
