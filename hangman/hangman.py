import random

def play_hangman():
    # Список слів
    word_list = ['python', 'java', 'javascript', 'php']

    # Випадково обираємо слово із списку
    secret_word = random.choice(word_list)

    # Максимальна кількість помилок
    max_attempts = 8

    # Кількість спроб, що залишилися
    attempts_left = max_attempts

    # Літери, які вже вгадані
    guessed_letters = set()

    # Рядок для відображення слова з дефісами
    word_display = '-' * len(secret_word)

    print("HANGMAN")
    print(word_display)

    while attempts_left > 0:
        print("Input a letter: > ", end="")
        user_input = input()

        if len(user_input) != 1:
            print("You should input a single letter")
            continue

        if not user_input.islower() or not user_input.isalpha():
            print("Please enter a lowercase English letter")
            continue

        if user_input in guessed_letters:
            print("You've already guessed this letter")
            continue

        if user_input in secret_word:
            guessed_letters.add(user_input)
            new_word_display = ""
            for i in range(len(secret_word)):
                if secret_word[i] in guessed_letters:
                    new_word_display += secret_word[i]
                else:
                    new_word_display += '-'
            if word_display == new_word_display:
                print("No improvements")
            else:
                word_display = new_word_display
        else:
            print("That letter doesn't appear in the word")

        print(word_display)
        print(f"Attempts left: {attempts_left}")

        if word_display == secret_word:
            print(f"You guessed the word {secret_word}!")
            print("You survived!")
            break

        attempts_left -= 1

    if word_display != secret_word:
        print(f"You lost! The word was {secret_word}")

def main():
    print("HANGMAN")
    while True:
        print('Type "play" to play the game, "exit" to quit: > ', end="")
        user_input = input()
        if user_input == "play":
            play_hangman()
        elif user_input == "exit":
            break

if __name__ == "__main__":
    main()
