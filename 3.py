# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open("text_3.txt", "r", encoding='utf-8') as workers:
    worker = workers.readlines()
    name_dict = {}
    for el in worker:
        el = el.split()
        el[1] = float(el[1])
        name_dict.update({el[1]: el[0]})
    for el in name_dict.keys():
        if el < 20000.0:
            print(name_dict.get(el))
    print("Средняя величина дохода: ", round(sum(name_dict.keys()) / len(name_dict), 2))
