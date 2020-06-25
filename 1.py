# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
# окончании ввода данных свидетельствует пустая строка.

# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

while True:
    with open("text.txt", "a", encoding='utf-8') as text:
        user_input = input("Введите строку. Для окончания нажмите Enter: ")
        if user_input == "":
            break
        print(user_input, file=text)
        print("Вы ввели: ", user_input)

with open("text.txt", "r", encoding='utf-8') as text:
    strings = text.readlines()
    print("Всего строк: ", len(strings))
    print("Всего слов в каждой строке (построчно):")
    for x, el in enumerate(strings, 1):
        print(x, len(el.split()))
