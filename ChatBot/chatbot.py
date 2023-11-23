# chatbot.py

# Отримання поточного року
from datetime import datetime

# Ім'я бота
bot_name = "DICT_Bot"

# Отримання поточного року
current_year = datetime.now().year

# Виведення привітання
print(f"Hello! My name is {bot_name}.")
print(f"I was created in {current_year}.")

# Запит імені користувача
print("Please, remind me your name.")
user_name = input()

# Виведення відповіді бота з ім'ям користувача
print(f"What a great name you have, {user_name}!")

# Вгадування віку користувача
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")

remainderr3 = int(input("Enter remainder when divided by 3: "))
remainderr5 = int(input("Enter remainder when divided by 5: "))
remainderrr7 = int(input("Enter remainder when divided by 7: "))

# Визначення віку за формулою
your_age = (remainderr3 * 70 + remainderr5 * 21 + remainderrr7 * 15) % 105

# Виведення віку, вгаданого ботом
print(f"Your age is {your_age}; that's a good time to start programming!")

# Підрахунок чисел від 0 до введеного користувачем числа
print("Now I will prove to you that I can count to any number you want.")
user_number = int(input("Enter a positive number: "))

for i in range(user_number + 1):
    print(f"{i} !")

# Тест з питаннями
print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")

# Перевірка відповіді користувача
while True:
    user_answer = input("Enter the number of your answer: ")
    if user_answer == "2":
        print("Congratulations, have a nice day!")
        break
    else:
        print("Please, try again.")
