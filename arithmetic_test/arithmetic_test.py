import random

def generate_question(level):
    if level == 1:
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)
        operator = random.choice(['+', '-', '*'])
        return f"{num1} {operator} {num2}", eval(f"{num1} {operator} {num2}")
    elif level == 2:
        num = random.randint(11, 29)
        return f"{num}^2", num ** 2

def check_answer(correct_answer):
    while True:
        user_answer = input("Enter your answer: ")
        if user_answer.isdigit():
            user_answer = int(user_answer)
            break
        else:
            print("Incorrect format. Try again.")
    if user_answer == correct_answer:
        print("Right!")
        return True
    else:
        print("Wrong!")
        return False

def save_result(name, mark, level):
    with open("results.txt", "a") as f:
        f.write(f"{name}: {mark}/5 in level {level} ({'simple operations with numbers 2-9' if level == 1 else 'integral squares of 11-29'})\n")

if __name__ == "__main__":
    print("Which level do you want? Enter a number:")
    print("1 - simple operations with numbers 2-9")
    print("2 - integral squares of 11-29")
    level = int(input("> "))

    correct_answers = 0

    for _ in range(5):
        question, correct_answer = generate_question(level)
        print(question)
        if check_answer(correct_answer):
            correct_answers += 1

    print(f"Your mark is {correct_answers}/5.")

    save_result_input = input("Would you like to save the result? Enter yes or no.\n> ").lower()
    if save_result_input in ["yes", "y"]:
        name = input("What is your name?\n> ")
        save_result(name, correct_answers, level)
