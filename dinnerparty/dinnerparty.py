import random

def main():
    # Зчитати кількість друзів, які бажають приєднатися
    num_friends = int(input("Enter the number of friends joining (including you):\n"))

    # Перевірити, чи кількість друзів коректна
    if num_friends <= 0:
        print("No one is joining for the party")
        return

    # Ініціалізувати словник для зберігання імен друзів та їх рахунком
    friends_dict = {}

    # Зчитати імена друзів і зберегти їх у словнику з рахунком 0
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(num_friends):
        friend_name = input("> ")
        friends_dict[friend_name] = 0

    # Зчитати загальний рахунок
    total_amount = float(input("Enter the total amount:\n"))

    # Перевірити, чи загальний рахунок коректний
    if total_amount <= 0:
        print("Invalid total amount")
        return

    # Запитати користувача, чи хоче він вибрати "щасливчика"
    lucky_choice = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No:\n")

    # Якщо користувач хоче вибрати "щасливчика"
    if lucky_choice.lower() == "yes":
        lucky_one = random.choice(list(friends_dict.keys()))
        print(f"{lucky_one} is the lucky one!")

        # Перерахувати суму для всіх, крім "щасливчика"
        for friend in friends_dict:
            if friend != lucky_one:
                friends_dict[friend] = round(total_amount / (num_friends - 1), 2)
            else:
                friends_dict[friend] = 0
    else:
        print("No one is going to be lucky")

    # Вивести оновлений словник
    print(friends_dict)

if __name__ == "__main__":
    main()
