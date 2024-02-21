import random

def computer_choice(options):
    return random.choice(options)

def find_winner(user_choice, comp_choice, options):
    if user_choice == comp_choice:
        return 'tie'
    elif (options.index(user_choice) + 1) % len(options) == options.index(comp_choice):
        return 'user'
    else:
        return 'computer'

def update_score(winner, score):
    if winner == 'user':
        return score + 100
    elif winner == 'tie':
        return score + 50
    else:
        return score

def read_rating(name):
    try:
        with open("rating.txt", "r") as f:
            for line in f:
                n, s = line.strip().split()
                if n == name:
                    return int(s)
        return 0
    except FileNotFoundError:
        return 0

def save_rating(name, score):
    with open("rating.txt", "a") as f:
        f.write(f"{name} {score}\n")

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(f"Hello, {name}")

    score = read_rating(name)

    options_input = input("Enter options separated by comma (or leave blank for default): ")
    options = options_input.split(',') if options_input else ['rock', 'paper', 'scissors']

    print("Okay, let's start.")

    while True:
        user_input = input().lower()

        if user_input == "!exit":
            print("Bye!")
            break
        elif user_input == "!rating":
            print(f"Your rating: {score}")
        elif user_input in options:
            comp_choice = computer_choice(options)
            winner = find_winner(user_input, comp_choice, options)

            if winner == 'user':
                print(f"Well done. The computer chose {comp_choice} and failed")
            elif winner == 'computer':
                print(f"Sorry, but the computer chose {comp_choice}")
            else:
                print(f"There is a draw ({user_input})")

            score = update_score(winner, score)
        else:
            print("Invalid input.")

    save_rating(name, score)
