import random

def play_21_game():
    current = 0
    print("Welcome to the 21 Number Game!")
    print("Players take turns adding 1, 2, or 3 to the current number.")
    print("The player who is forced to say 21 loses.\n")

    # Determine who starts first
    first = input("Do you want to go first? (y/n): ").lower()
    player_turn = True if first == 'y' else False

    if player_turn:
        print("You start first.")
    else:
        print("Computer starts first.")

    while True:
        if player_turn:
            # Player's turn
            print(f"\nCurrent number: {current}")
            move = input("Your move (1, 2, 3): ")

            # Validate input
            if move not in ['1', '2', '3']:
                print("Invalid input. Please enter 1, 2, or 3.")
                continue

            move = int(move)

            # Check if player says 21
            if current + move >= 21 and current < 21:
                print(f"\nYou said numbers {current+1} to {current+move}...")
                print("You said 21! You lose.")
                return

            current += move
            print(f"You added {move}. New total: {current}")
            player_turn = False

        else:
            # Computer's turn
            if current % 4 == 0:  # Computer is in losing position
                move = random.randint(1, 3)
            else:  # Optimal move
                move = 4 - (current % 4)

            # Check if computer says 21
            if current + move >= 21 and current < 21:
                print(f"\nComputer says numbers {current+1} to {current+move}...")
                print("Computer said 21! Computer loses. You win!")
                return

            current += move
            print(f"Computer adds {move}. New total: {current}")
            player_turn = True

if __name__ == "__main__":
    play_21_game()
