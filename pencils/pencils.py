import random

def validate_input(input_str, min_val, max_val):
    try:
        value = int(input_str)
        if min_val <= value <= max_val:
            return value
        else:
            print(f"Input must be an integer between {min_val} and {max_val}.")
    except ValueError:
        print("Invalid input. Please enter an integer.")
    return None

def bot_turn(pencils):
    if pencils % 4 == 0:
        return random.randint(1, 3)
    else:
        return pencils % 4

def main():
    print("How many pencils would you like to use:")
    pencils = validate_input(input(), 1, float('inf'))
    if pencils is None:
        return

    players = ["John", "Jack"]
    print(f"Who will be the first ({players[0]}, {players[1]}):")
    first_player = input()
    if first_player not in players:
        print(f"Choose between '{players[0]}' and '{players[1]}'")
        return

    print("|" * pencils)

    player_index = 0 if first_player == players[0] else 1

    while pencils > 0:
        if player_index == 0:  # Human's turn
            print(f"{players[player_index]}'s turn:")
            taken = validate_input(input(), 1, min(3, pencils))
            if taken is not None:
                pencils -= taken
                print("|" * pencils)
                if pencils == 0:
                    print(f"{players[player_index]} won!")
                    break
        else:  # Bot's turn
            print(f"{players[player_index]}'s turn:")
            taken = bot_turn(pencils)
            pencils -= taken
            print("|" * pencils)
            if pencils == 0:
                print(f"{players[player_index]} won!")
                break

        player_index = (player_index + 1) % 2  # Switch player

if __name__ == "__main__":
    main()
