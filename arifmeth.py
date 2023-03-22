import random

def generate_problem(level):
    if level == 1:  # очень простые примеры
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        operator = random.choice(['+', '-'])
        problem = f"{a} {operator} {b}"
        answer = eval(problem)
    elif level == 2:  # средние примеры
        a = random.randint(0, 50)
        b = random.randint(0, 50)
        operator = random.choice(['+', '-', '*'])
        problem = f"{a} {operator} {b}"
        answer = eval(problem)
    elif level == 3:  # сложные примеры
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        operator1 = random.choice(['+', '-'])
        operator2 = random.choice(['+', '-'])
        problem = f"{a} {operator1} {b} {operator2} {a}"
        answer = eval(problem)
    else:  # уровень 4: смешанные примеры
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        c = random.randint(0, 10)
        operator1 = random.choice(['+', '-', '*'])
        operator2 = random.choice(['+', '-', '*'])
        problem = f"{a} {operator1} {b} {operator2} {c}"
        answer = eval(problem)

    return problem, answer

def main():
    print("Выберите уровень сложности: 1-4")
    level = int(input())

    num_problems = 10  # сколько примеров нужно решить
    correct_answers = 0

    for i in range(num_problems):
        problem, correct_answer = generate_problem(level)

        # Выводим пример и ждем ввода ответа
        print(f"Пример {i + 1}: {problem}")
        user_answer = input("Введите ответ: ")

        # Проверяем ответ пользователя
        if float(user_answer) == float(correct_answer):
            print("Правильно!")
            correct_answers += 1
        else:
            print(f"Не правильно! Правильный ответ: {correct_answer}")

    # Выводим результаты
    print(f"Вы решили {correct_answers} из {num_problems} примеров!")

if __name__ == "__main__":
    main()