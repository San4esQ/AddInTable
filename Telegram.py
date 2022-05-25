import random
Help = """
help - напечатать справку по программе.
add - добавить задачу в список. 
show - напечатать все добавленные задачи.
exit - выход.
random - добавлять случайную задачу на дату Сегодня"""

random_tasks = ["Убраться в квартире", "Позвонить маме", "Поиграть с друзьями", "Помыть машину", "Приготовить покушать"]

tasks = {}

run = True

def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)
    print("Задача ", task, " добавлена на дату - ", date)

while run:
    command = input("Введите команду: ")
    if command == "help" :
        print(Help)
    elif command == "show" :
        date = input("Введите дату для отображения списка задач: ")
        if date in tasks:
            for task in tasks[date]:
                print('-',task)
        else:
            print("Такой даты нет")
        print(tasks)
    elif command == "add" :
        date = input("Введите дату для добавления задачи: ")
        task = input("Введите название задачи: ")
        add_todo(date, task)
    elif command == "random":
        task = random.choice(random_tasks)
        add_todo("Сегодня", task)
    elif command == "exit" :
        run = False
        print("До свидания!")
    else:
        print("Неизвестная команда. Попробуйте еще раз: ")
        continue

